
# *IMPORT* is how you add modules/libraries to your script from the Python feature set.
# Rather than give you all the modules/libraries at once, Python asks you to say what
# you plan to use. This keeps your programs small, but it also acts as 
# documentation for other programmers who read your code later.

# *argv* is the "argument variable". It holds the arguments you pass to your
# Python script when you run it. 

from sys import argv 

# This line unpacks *argv* so that rather than holding all the arguments, it gets
# assigned to four variables: script, first, second, and third. In other words,
# this means to "take whatever is in *argv*, unpack it, and assign it to all these
# variables on the left in order"
script, first, second, third = argv

# Run as *python3 ex13.py first 2nd 3rd*
# this will print: "
# The script is called ex13.py
# Your first variable is first
# Your second variable is 2nd
# Your third variable is 3rd"

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)