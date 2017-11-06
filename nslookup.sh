#!/bin/bash
echo "This program is used to LOOKUP DNS resolution of a hostname input through a text file. The text file should contain individual hostnames on a new line."
echo
echo -n "Enter the file path for host list: "
read list
file=$list
while IFS= read -r line
do
       #echo $line "resolves to" `nslookup $line | awk '!/#53/ && /Address/ { print $2 }'`
	echo `nslookup $line | awk '!/#53/ && /Address/ { print $2 }'`
done <"$file"
