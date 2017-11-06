#!/bin/bash

# Replace the 'path to awsiprange.txt' with the name of the file you want to store AWS ip ranges to.
awsiprange="/path/to/awsiprange.txt"

# For every IPaddress extracted from the AWS range available on the URL, check if the IP already in our destination file.
# If not, then append/add the IP to the file.
for ip in `curl https://ip-ranges.amazonaws.com/ip-ranges.json 2>/dev/null | grep -oP 'ip_prefix": "\K[^"]*'`
do
        if grep -Fxq "$ip" $awsiprange
        then
                continue
        else
                echo "$ip" >> $awsiprange
        fi
done
