import re
import os

# Define regex to find any pattern of an IPv4 address pattern.
r = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

# Function to validate if the IPv4 address is valid or not.
# Each octet should be a number between 0 - 255 for it to be valid IPv4 address.
def validate_ip(ip):
	s = ip.split('.')
	for x in s:
		y = int(x)
		if y < 0 or y > 255:
			return False
	return True

# Initialize list to store valid IPv4 addresses.
ip_list = []

# Parse through the directories recursively to identify files.
# Give the path of the parent directory that you want to scan recursively in 'os.walk'
for root, dirs, files in os.walk("/home/user"):
	for name in files:
		# Open the files in READ mode using the absolute path of the file in each loop/recursion.
		input_file = os.path.abspath(os.path.join(root, name))
		f = open(input_file, 'r')
		lines = f.readlines()
		# Parse each file one line at-a-time and match regex of IPv4 address pattern.
		for line in lines:
			i = r.findall(line)
			# For any IPv4 address pattern match, check if the IP is valid and if already exists in our list.
			# If the IP is valid and is not a duplicate entry, append it to our list of stored IPv4 addresses.
			for ip in i:
				if ip is not None and validate_ip(ip) is True and ip not in ip_list:
					ip_list.append(ip)
		f.close()

# The sorted() function automatically sorts the IP addresses lexicographically using the first octet.
s = sorted(ip_list)

# Join and print the sorted list.
output = '\n'.join(s)
print output