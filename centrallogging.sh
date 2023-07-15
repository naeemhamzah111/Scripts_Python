#! /bin/bash

# script for central logging it will check for new errors live and output it to a file 


tail -fn0 /var/log/messages | while read line

do 
	echo $line | egrep -i "refused|invalid|error|fail|lost|shut|down|offline"
	if [ $? = 0 ]
	then
		echo $line >> /tmp/filtered-messages
	fi
done
