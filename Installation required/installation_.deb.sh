#!/bin/bash

sudo apt update ; sudo apt upgrade -y ; sudo apt-get update ; sudo apt-get upgrade -y ;

sudo apt install python3 -y
sudo apt install python3-pip -y

sudo apt update ; sudo apt upgrade -y ; sudo apt-get update ; sudo apt-get upgrade -y ;

pip3 install sockets
pip3 install dnspython
pip3 install requests

sudo apt update ; sudo apt upgrade -y ; sudo apt-get update ; sudo apt-get upgrade -y ;
sudo apt autoremove -y ; sudo apt autoclean -y

echo ''
echo '------ Install Completed ------'
echo ''
