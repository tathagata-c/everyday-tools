# Parse through multiple '.log' files. Find the most common ERROR by analyzing the log files,
# sorted by the number of errors in descending order. If two source files have the same number of errors,
# the file with the lexicographically smallest name should go first.
# Sample LOG structure - timestamp|log_type|source_file_name|line|function_name|log_text
# timestamp is a unix time stamp; source_file_name, function_name and log_text can be any sequence of symbols;
# line is non-negative integer; log_type is one of the following values: ERROR, WARNING, TRACE, INFO.

import os

# Initialize lists to store source-files by error, list of unique source-file names
# and store error count of each unique source-file.
error_list = []
unique_list = []
count_list = []

# Parse through the directories recursively to identify files ending with .log extension.
for root, dirs, files in os.walk("/home/user"):
	for name in files:
		if name.endswith(".log"):
			input_file = os.path.abspath(os.path.join(root, name))
			# Open the files in READ mode using the absolute path of the file in each loop/recursion.
			f = open(input_file, 'r')
			lines = f.readlines()
			# Parse each file one line at-a-time and split them using '|' as delimiter.
			# If ERROR string is found in the second element, store the third element, i.e. source-file in error_list.
			for line in lines:
				a = line.split("|")
				if a[1] == "ERROR":
					error_list.append(a[2])
			f.close()

# Store unique source-file names in unique_list.
for item in error_list:
	if item not in unique_list:
		unique_list.append(item)

# Store the error count of each unique source-file in count_list. 
for a in unique_list:
	count_list.append(error_list.count(a))

# Store source-file and respective error count as tuples in a list.
list = zip(unique_list, count_list)

# Sort the list using a key of source-filename initially.
list = sorted(list, key = lambda x: (x[0]))

# Sort the list again using a key of count in descending order.
list = sorted(list, key = lambda x: (x[1]), reverse=True)

# Print the Tuple elements in the sorted list on new lines.
print "\n".join([ "%s %s" % x for x in list ])