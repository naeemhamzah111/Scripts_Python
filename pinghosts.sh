#! /bin/bash

# pinging a remote host and notify

read -p "Enter IP addresses (space-separated): " -a IPADD

for i in ${IPADD[@]}; 
do
ping -c5 "$i" &> /dev/null
	if [ $? -eq 0 ]
	then 
	echo its Good can connect
	else   
	echo Not good cannot connect
	fi
done

