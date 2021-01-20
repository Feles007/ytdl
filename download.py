from subprocess import call

# Get data from file
with open(input("Input File: ")) as input_file:
	input_data = input_file.readlines()
# Strip \n
for i in range(len(input_data)):
	input_data[i] = input_data[i].strip()
# Pre and post initialization
pre = ""
post = ""
pre_flag = 0
post_flag = 0
# Download constructed urls
for item in input_data:
	if pre_flag == 0 and post_flag == 0:
		if item != "":
			if item[0] != "$":
				constructed_url = pre + item + post
				command = ["youtube-dl", constructed_url]
				call(command)
			else:
				if item.lower() == "$pre":
					pre_flag = 1
				if item.lower() == "$post":
					post_flag = 1
	else:
		if pre_flag == 1:
			pre = item
			pre_flag = 0
		if post_flag == 1:
			post = item
			post_flag = 0