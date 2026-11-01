#!/bin/bash

set -eux

dnf update -y
dnf install -y git docker

systemctl enable docker
systemctl start docker

mkdir -p /usr/local/lib/docker/cli-plugins

curl -L \
https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 \
-o /usr/local/lib/docker/cli-plugins/docker-compose

chmod +x /usr/local/lib/docker/cli-plugins/docker-compose

curl -L \
https://github.com/docker/buildx/releases/latest/download/buildx-linux-amd64 \
-o /usr/local/lib/docker/cli-plugins/docker-buildx

chmod +x /usr/local/lib/docker/cli-plugins/docker-buildx

cd /home/ec2-user

git clone https://github.com/sandy989/kafka_learning_project.git

cd kafka_learning_project

docker compose up -d --build