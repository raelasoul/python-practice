# open a file and print it out without "hard coding" the name of the file in the program
# use *argv* or *input* to ask the user what file to open instead of hardcoding file's name

# Lines 5-6 uses argv to get a filename
from sys import argv
script, filename = argv

# This line uses a command to open file 
# the file is then stored in *txt* variable
txt = open(filename)

# Prints the name of the file 
print(f"Here's your file {filename}:")

# Prints/displays contents of file
# The function read() is called on the *txt* variable
print(txt.read())
print(txt.close())

# Repeats the top part of the program, but receives file input from user
# instead of passing in an argument
# stores the input of the file name into variable *file_again*
# *file again* is then opened, creates a file object, and then stored into *txt_again* variable
# and the it is read and printed
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

print(txt_again.close())