# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
#
#
#
#

# Your code here.

import os
def rename_files():
	#(1) get file names from a folder
	file_list = os.listdir(r"C:\Users\Gloria\Documents")
	print (file_list)
	os.chdir(r"C:\Users\Gloria\Documents")
	#(2) for each file, rename filename
	for file_name in file_list:
		os.rename(file_name,file_name.translate(None, "1234567890"))

rename_files()