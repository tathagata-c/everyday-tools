#!/bin/bash

awsiprange="/path/to/awsiprange.txt"
for ip in `curl https://ip-ranges.amazonaws.com/ip-ranges.json 2>/dev/null | grep -oP 'ip_prefix": "\K[^"]*'`
do
        if grep -Fxq "$ip" $awsiprange
        then
                continue
        else
                echo "$ip" >> $awsiprange
        fi
done
