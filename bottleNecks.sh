#!/bin/bash

#Health Check Script
#Utilize Variables to Output Status of Machine

#Uptime

uptime

#Memory
memory_total=$(free -m | awk '/Mem:/ {print $2}')
memory_used=$(free -m | awk '/Mem:/ {print $3}')
memory_free=$(free -m | awk '/Mem:/ {print $4}')

#echo "Memory Total: $memory_total"
#echo "Memory Used: $memory_used"
#echo "Memory Free: $memory_free"

memory_percent_raw=$(echo "scale=2; $memory_used/$memory_total" | bc)
memory_percent=$(echo "$memory_percent_raw*100/1.00" | bc)
memory_check=25

#echo "Memory Percent Utilization: $memory_percent%"

if [ $(echo "$memory_percent < $memory_check" ) ];
then
	echo "Memory Availbility is Healthy. Less than $memory_check% Utilzation"
else
	echo "Memory Availability is Unhealthy. More than $memory_check% Utilzation"
fi

#CPU

#Disk Df-h

a=$(df -h | egrep -v "tmpfs|devtmpfs" | awk '{print $5}' | cut -d '%' -f1 | grep -Eo '[0-9]+')  
b=$(df -h | egrep -v "tmpfs|devtmpfs|Filesystem" | awk '{print $1}')

for i in $a

do
	if (($i >= 30));
        
	then
                echo "check disk space it is: $i% for disk: $b"
        else
                echo "Using df, the disk space is under 30%: $i% for disk: $b"
 	fi
done

#Disk
Disk_Device=$(iostat -m | egrep -v "avg-cpu|Device|Linux|2.40" | awk '{print $1}')

for i in $Disk_Device

do
	echo $Disk_Device(i)
done


#Ping

#Networking
