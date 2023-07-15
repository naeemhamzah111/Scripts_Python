#! /bin/bash

#df -h | egrep -v "tmpfs|devtmpfs" | awk '{print $5}'| cut -d '%' -f1

read -p " enter ipadresses you want to check" -a IPADD

for IPs in "${IPADD[@]}"; 
do 
	diskspace=$(ssh "$IPs" "df -h | egrep -v "tmpfs|devtmpfs" | awk '{print \$5}'| cut -d '%' -f1") 

if      ["$diskspace" -eq 5]; 
then 
	echo the script works
else 
	echo this script doesnt work
fi
done


