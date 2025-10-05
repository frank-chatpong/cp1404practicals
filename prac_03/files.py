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

# 2. In the same file, but as if it were a separate program, write code that opens "name.txt"
# and reads the name (as above) then prints (note the exact output),
# Hi Bob! (or whatever the name is in the file). Do not simply print the user's input variable!
# Use open and close for this question.

"""Open the file and read the name"""
in_file = open("name.txt", 'r')
name = in_file.read().strip()
in_file.close()

print(f"Hi {name}!")
