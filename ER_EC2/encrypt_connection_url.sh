#!/bin/bash
sudo chmod +x encrypt.py

EC2_DB_CONNECTION_STRING=$1
READ_EC2_DB_CONNECTION_STRING=$2

python encrypt.py --w  $EC2_DB_CONNECTION_STRING --r $READ_EC2_DB_CONNECTION_STRING