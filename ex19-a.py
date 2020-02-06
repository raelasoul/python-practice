# my function

def carlasFunction (age, city):
    print(f"My name is Carla and I am {age} years old.")
    print(f"I live in {city}, Louisiana. ")

carlasFunction(32, "Baton Rouge")
print("\n")

# -----------------------------
carlasFunction (30 + 2, "Baton Rouge")
print("\n")

# -----------------------------
#variables
print("Use variables to pass to function:\n")
my_age = 10+20+2
my_city = "Baton Rouge"

carlasFunction(my_age, my_city)

# -----------------------------
# multiple variables
print("\nWill do the calculations using multiple variables\n")

# calculate my age
# storing my birth year and current year in variables and using math to calculate my age and storing it in a variable
birth_year = 1987
current_year = 2020
current_age = current_year - birth_year

print(f"I was born in {birth_year}")
print(f"The current year is {current_year}")
print (f"Since I was born in {birth_year} and the current year is {current_year}, that makes me {current_age} years old.\n")

# city that I live in
# storing Baton and Rouge in different variables then concatenating them and storing them in a different variable "both_words"
first_word = "Baton"
second_word = "Rouge"
both_words = first_word + " " + second_word

print(f'In French, {first_word} means "stick" and {second_word} mean "red."\n')
print(f'My city is known as "The Red Stick" aka {both_words}.')
print("..now lets pass this to the function and print..\n")

carlasFunction(current_age, both_words)

# -----------------------------
# prompt the user and pass to function
print("""\nNow I want to prompt the user to answer questions. The input received will be stored in variables
that will be passed to the function.
""")

# Take the age input and store it in a variable. Input will need to be converted to int since it is a number
# Take the city input and store it in a variable.
ageInput = int(input("How old are you? "))
input("> Press Enter")
cityInput = input("What city do you currently live in? ")
input("> Press Enter")

carlasFunction(ageInput, cityInput)