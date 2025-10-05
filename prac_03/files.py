"""
CP1404/CP5632 - Practical
Complete the tasks from the following questions
"""

# 1. Write code that asks the user for their name, then opens a file called name.txt
# and writes that name to it. Use open and close for this question.

"""Ask the user for their name and write in the file"""
name = input("Write your name: ")

out_file = open("name.txt", 'w')
print(name, file=out_file)

out_file.close()
