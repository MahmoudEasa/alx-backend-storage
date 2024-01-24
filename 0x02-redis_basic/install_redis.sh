#!/usr/bin/env bash
# Install Redis on Ubuntu 18.04
sudo apt-get -y install redis-server
pip3 install redis
sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

