# Barbara Garr
# 13 November 24
# P1HW2
# This program to calculates and displays a travel budget based on user input.

# pseudocode
# Display "This program calculates and displays travel expenses"
# Ask user "Enter Budget"
# Input Budget
# Ask user "Enter your travel destination"
# Input Destination
# Ask user "How much do you think you will spend on gas?"
# Input Fuel
# Ask user "Approximately, how much will you need for accomodation/hotel?"
# Input Hotel
# Ask user "Last, how much do you need for food?"
# Input Food
# Display "-------------Travel Expenses------------"
# Display "Location:", destination
# Display "Initial Budget:", budget
# Display "Fuel:", fuel
# Display "Accomodation:", hotel
# Display "Food:", food
# Set expenses = fuel + hotel + food
# Set remaining_balance = budget - expenses
# Display "Remaining Balance:", remaining_balance

print('This program calculates and displays travel expenses')
budget = float(input('\nEnter Budget: '))
destination = input('\nEnter your travel destination: ')
fuel = float(input('\nHow much do you think you will spend on gas? '))
hotel = float(input('\nApproximately, how much will you need for accomodation/hotel? '))
food = float(input('\nLast, how much do you need for food? '))
print('\n-------------Travel Expenses------------')
print('Location: ', destination)
print('Initial Budget: ', budget)
print('\nFuel: ', fuel)
print('Accomodation: ', hotel)
print('Food: ', food)
expenses = fuel + hotel + food
remaining_balance = budget - expenses
print('\nRemaining Balance: ', remaining_balance)


