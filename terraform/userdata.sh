#!/bin/bash

set -e

dnf update -y

dnf install git docker -y

systemctl enable docker
systemctl start docker

usermod -aG docker ec2-user

dnf install docker-compose-plugin -y

cd /home/ec2-user

git clone ${github_repo}

REPO_NAME=$(basename ${github_repo} .git)

cd ${REPO_NAME}

docker compose up -d --build

docker ps