#!/bin/bash
echo 
echo "This program is used to LOOKUP DNS resolution of an IP address input through a text file. The text file should contain individual IP addresses on a new line."
echo 
echo -n "Enter the full path of the IP list: "
read list
file=$list
while IFS= read -r line
do
        echo $line "resolves to" `nslookup $line | awk '/name/ { print $4 }' | sed 's/.$//'`
done <"$file"
