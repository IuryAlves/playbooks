#!/usr/bin/env python
# coding: utf-8


import json
import os
import sys
import time
import click
import boto3

EC2_RUNNING_STATE = '16'
DESCRIBE_INSTANCES_COUNTDOWN = 10

ec2 = boto3.client('ec2')


def _describe_instances(ec2_tag_name=None, ec2_tag_value=None):
    count = 0
    filters = [
        {
            'Name': 'instance-state-code',
            'Values': [EC2_RUNNING_STATE]
        }
    ]
    if all([ec2_tag_name, ec2_tag_value]):
        ec2_tag_name = 'tag:{0}'.format(ec2_tag_name)
        filters.append({
            'Name': ec2_tag_name,
            'Values': [ec2_tag_value]
        })

    response = ec2.describe_instances(Filters=filters)
    while not response.get('Reservations') and count < DESCRIBE_INSTANCES_COUNTDOWN:
        time.sleep(5)
        response = ec2.describe_instances(Filters=filters)
        count += 1
    return response


def _list(ec2_tag_name, ec2_tag_value):

    output = {
        'servers': []
    }
    response = _describe_instances(ec2_tag_name, ec2_tag_value)
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if 'PrivateIpAddress' in instance:
                output['servers'].append(instance['PrivateIpAddress'])

    return output


def _hosts():
    # No need to return host information
    return {}


@click.command()
@click.option('--list', default=False, is_flag=True)
@click.option('--host', default=None)
def main(**kwargs):
    host = kwargs.get('host')
    list_ = kwargs.get('list')

    ec2_tag_name = os.getenv('ANSIBLE_EC2_TAG_NAME')
    ec2_tag_value = os.getenv('ANSIBLE_EC2_TAG_VALUE')

    if list_ and host is None:
        result = _list(ec2_tag_name, ec2_tag_value)
    else:
        result = _hosts()
    json.dump(result, sys.stdout)


if __name__ == '__main__':
    main()
