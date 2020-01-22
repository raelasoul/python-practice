# Excercise 4: Variables and Names

# 100 cars
cars = 100

#4.0 is a floating number assigned to space_in_a_car
space_in_a_car = 4.0

# 30 drivers
drivers = 30

# 90 passengers
passengers = 90

# the amount of cars (100) minus the amount of drivers (30) is assigned: 70
cars_not_driven = cars - drivers

# the amount of drivers (30) is assigned to the amount of cars that are driven
cars_driven = drivers

#carpool_capacity will equal the total amount of cars_driven (drivers = 30) plus the amount of space_in_a_car (4.0): 34.0
carpool_capacity = cars_driven + space_in_a_car

#the average_passengers_per_car equals passengers (90) divided by cars_driven (drivers = 30): 3
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
