#!/bin/bash

#Ping Each IP Seperated by Lines in a given .txt file

for i in $(cat IP_Test.txt)
do
    ping -c1 $i
done


