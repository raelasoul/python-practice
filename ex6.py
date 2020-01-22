# Study Drills:
# 1. Go through this program and write a comment above each line explaining it.
# 2. Find all the places where a string is put inside a string. There are four places.
# 3. Are you sure there are only four places? How do you know? Maybe I like lying.
# 4. Explain why adding the two strings w and e with + makes a longer string.

# The variable types_of_people has the value 10 assigned to it
types_of_people = 10

# x is a variable that contains a formatted string. The formatted string includes the 
# variable types_of_people that has the value of 10 assigned to it
# string within string
x = f"There are {types_of_people} types of people."

# binary variable holds the string "binary"
binary = "binary"

# do_not variable holds the string "don't"
do_not = "don't"

# y is a variable that contains a formatted string. The formatted string includes two 
# variables: binary and do_not
# string within string
y = f"Those who know {binary} and those who {do_not}."

# prints the contents assigned the variables x and y
print(x)
print(y)

# string within string
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# string within a string - prints the string that is assigned to *joke evaluation* and then includes 
# the value assigned to hilarious but converts the format to a string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# concetenation of strings that are assigned to variable w and variable e
print(w + e)