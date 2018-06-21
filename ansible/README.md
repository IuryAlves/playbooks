Ansible Playbooks
=================

## Installing

* Be sure that you have run `install.sh` before using ansible.

Then run:

    ansible/extensions/setup/update_roles.sh

### Credentials

You will need:

* ansible-vault-password


1. Create a file called `vault_pass.txt` in your home directory
2. Insert your `ansible-vault` password there.

*If you don't have `ansible-vault` password, ask for your sysadmin.


## Testing

#### Requirements:

* Vagrant with virtualbox provider


We use vagrant to set up our test servers. Install vagrant and run the following commands under this directory:

1. Start the virtual machine

		vagrant up

2. Getting ssh information

		vagrant ssh-config

It should output something like:

```
Host default
  HostName 127.0.0.1
  User vagrant
  Port 2222
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile /home/yori/projects/devops/ansible/.vagrant/machines/default/virtualbox/private_key
  IdentitiesOnly yes
  LogLevel FATAL
```

3. Create a file called `ansible.cfg` with the following content:


```
[defaults]
hostfile=inventory/development.hosts
remote_user=vagrant
private_key_file=<vagrant-identity-file>
host_key_checking=False
roles_path=roles/internal:roles/external
```

4. Change `<vagrant-identity-file>` with the IdentityFile output by the step 2.

5. Testing:

	ansible testserver -m ping

If everithing went well you should see the following:

```
vagrant | success >> {
    "changed": false,
    "ping": "pong"
}
```

## Testing

You can run, for example:

	ansible-playbook playbooks/jenkins/main.yml --vault-password-file=~/vault_pass.txt


**The organization of this repo in based upon [Ansible best practices](https://github.com/enginyoyen/ansible-best-practises)**