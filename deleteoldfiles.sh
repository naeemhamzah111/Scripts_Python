#! /bin/bash

# we will find old files older then three months then we will delete them 

find /home/partha -mtime +90 -exec rm {} \; 
