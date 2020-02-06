# FUNCTIONS & VARIABLES
# 
# Variables in the function are different from others that are listed below
# cheese_count and boxes_of_crackers can accept values that are assigned to 
# variables. (i.e., cheese_count can be passed the value that is assigned to amount_of_cheese)

# define function, indicate arguments
# indicate what is performed in this function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Method 1:
# directly gives the function the numbers
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# uses variables to pass to the function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# ---------------------------------
# Method 2:
# function is called and variables are the arguments of the function
# this will print:
# "You have {10} cheeses (amount_of_cheese = 10)
# You have {50} boxes of crackers (amount_of_crackers = 50)
# Man that's enough for a party!
# Get a blanket."
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# ---------------------------------
#Method 3:
# using math and passing to function
# this will plug in the calculations in function
# 10 + 20 = amount_of_cheese
# 5 + 6 = amount_of_crackers
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# ---------------------------------
# Method 4:
# uses variables and math
# this will take 110 (amount_of_cheese + 100)
# and 1050 (amount_of_crackers + 1000) and plug into
# {cheese_count} and {boxes_of_crackers}
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)