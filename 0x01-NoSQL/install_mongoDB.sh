#!/usr/bin/env bash

# Install MongoDB 4.4 in Ubuntu 20.04
echo "Touch /etc/apt/sources.list.d/mongodb-org-4.4.list:"
echo
sudo touch /etc/apt/sources.list.d/mongodb-org-4.4.list
echo
echo

echo "Import the MongoDB repository GPG key:"
echo
sudo wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo
echo

echo "Add the MongoDB repository to the package sources list:"
echo
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
echo
echo

echo "Update the package lists:"
echo
sudo apt-get update
echo
echo

echo "Install MongoDB:"
echo
sudo apt-get install -y mongodb-org
echo
echo

echo "Start MongoDB:"
echo
sudo service mongod start
echo
echo

echo "MongoDB Status:"
echo
sudo service mongod status | less -FX
echo
echo

echo "MongoDB Version:"
echo
mongo --version | less -FX
echo
echo

# Install PyMongo
echo "Install PyMongo"
echo
pip3 install pymongo
echo
echo

