# Lesson 3.2: Use Functions
# Mini-Project: Take a Break

# Write a program that prompts the user to take a break
# once every two hours, a maximum of three times.

# Use this space to describe your approach to the problem.
#
#
#
#

# Your code here.
import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
while (break_count < total_breaks):
	time.sleep(10)
	webbrowser.open("gttp://www.youtube.com/watch?v-dQw4w9WgXcQ")
	break_count += 1