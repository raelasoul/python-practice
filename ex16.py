# 16 - Reading and Writing Files
# text editor

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

# opens file that was specified as argument through bash: [python ex16.py ex15_sample.txt]
# sets command to write using 'w'
print("Opening the file...")
target = open(filename, 'w')

# truncate : resizes file to the given number of bytes. if size is not specified, the current 
# position is used.
print("Truncating the file. Goodbye!")
target.truncate()

# this is where the user will write to the file
# user is asked to input information on three lines
# information is stored in variables: line1, line2, & line3
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# information stored in variables line1-3 are written to file and 
# separated by a new line
target.write(line1, end="\n")
#target.write("\n")
target.write(line2, end="\n")
#target.write("\n")
target.write(line3, end="\n")
#target.write("\n")

# file is closed
print("File is closing.")
target.close()

# Prints the name of the file 
print(f"Here are the contents of {filename}:")

# *Study Drill #2*
# opens file that was just written.
# contents of file are displayed.
file = open("ex15_sample.txt", 'r')

# uses for loop : for every line in the file, print that line
# more memory efficient, and fast manner, you can use the loop over method. 
# The advantage to using this method is that the related code is both simple and easy to read. 
# via https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
for line in file:
        print (line)




