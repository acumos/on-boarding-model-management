#!/usr/bin/bash

cd /opt/app/anaconda2

export http_proxy=http://one.proxy.att.com:8080
export https_proxy=http://one.proxy.att.com:8080
export no_proxy=.att.com,localhost,127.0.0.1

export PATH=/opt/app/anaconda2/python36/bin:$PATH

#pip install /opt/app/microservice/requirements

pip install -e /opt/app/microservice

mkdir -p /log

cd /opt/app/microservice

gunicorn --timeout 120 --bind 0.0.0.0:8081 --config /opt/app/microservice/properties/config.ini wsgi:application
#python run.py

