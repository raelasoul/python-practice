name = 'Carla R. Buckner'
age = 32 
height = 67 # inches
weight = 180 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print(f"Hi, I'm {name}.")
print(f"I am {height} inches tall.")
print(f"I am {weight} pounds.")
print("That's expected to change soon!")
print(f"I've got {eyes} eyes and {hair} hair.")
print(f"My teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

#convert inches to pounds
inches_to_centimeters = height * 2.54
print(f"My height is {height}in, but when converted to centimeters, it is {inches_to_centimeters}cm")

pounds_to_kilos = weight / 2.205
print(f"My weight is {weight}lbs, but when converted to kilograms, it is {pounds_to_kilos}kg")
