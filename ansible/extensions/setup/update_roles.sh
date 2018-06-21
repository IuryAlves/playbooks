#!/usr/bin/env sh

BASE_DIR="$(git rev-parse --show-toplevel)"

ROLE_REQUIREMENTS_FILE=ansible/roles/roles_requirements.yml
EXTERNAL_ROLE_DIR=ansible/roles/external

ansible-galaxy install -r "${ROLE_REQUIREMENTS_FILE}" --force --no-deps -p "${EXTERNAL_ROLE_DIR}"