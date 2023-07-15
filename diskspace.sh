#! /bin/bash

#df -h | egrep -v "tmpfs|devtmpfs" | awk '{print $5}'| cut -d '%' -f1

a=$(df -h | egrep -v "tmpfs|devtmpfs" | awk '{print $5}' | cut -d '%' -f1 | grep -Eo '[0-9]+')

if [[ -n $a ]]; then
    if ((a >= 30)); then
        echo "Check disk space: $a%"
    else
        echo "Using df, the disk space is under 30%: $a%"
    fi
fi
	

