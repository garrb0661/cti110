# Barbara Garr
# 19 November 2024
# P2LAB2
# This program calculates the amount of gas needed in gallons based on user input.

# Pseudocode
# Set the dictionary of cars
cars_dict = {"Camaro":18.21,
        "Prius":52.36,
        "Model S":110,
        "Silverado":26
        }

# Set the keys for the dictionary
keys = cars_dict.keys()

# Display the keys
print(keys)

# Ask the user "Enter a vehicle to see it's mpg: "
car_chosen = input("\nEnter a vehicle to see it's mpg: ")
# Input car_chosen

# Display "The, car_chosen, gets, cars_dict[car_chosen], mpg."
print("\nThe",car_chosen,"gets",cars_dict[car_chosen],"mpg.")

# Ask the user "How many miles will you drive the {car_chosen}?"
miles = int(input(f"\nHow many miles will you drive the {car_chosen}? "))
# Input miles

# Set gallons = miles / cars_dict[car_chosen]
gallons = miles / cars_dict[car_chosen]

# Display "{gallons} gallon(s) of gas are needed to drive the {car_chosen} {miles} miles." Gallons floating point value is 2
print(f"\n{gallons:.2f} gallon(s) of gas are needed to drive the {car_chosen} {miles} miles.")
