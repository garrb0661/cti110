# Barbara Garr
# 26 November 24
# P2HW1
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
# Display "-" *15, "Travel Expenses", "-" * 16
# Display "Location:", destination.
# Display "Initial Budget:", budget. Budget floating point value is 2.
# Display "Fuel:", fuel. Fuel floating point value is 2.
# Display "Accomodation:", hotel. Hotel floating point value is 2.
# Display "Food:", food. Food floating point value is 2.
# Calculate expenses by adding fuel, hotel, and food together
# Calculate remaining_balance by subtracting the expenses from the inital budget
# Display "-" *48
# Display "Remaining Balance:", remaining_balance. remaining_balance floating point value is 2.

print('This program calculates and displays travel expenses')
budget = float(input('\nEnter Budget: '))
destination = input('\nEnter your travel destination: ')
fuel = float(input('\nHow much do you think you will spend on gas? '))
hotel = float(input('\nApproximately, how much will you need for accomodation/hotel? '))
food = float(input('\nLast, how much do you need for food? '))
print()
print('-'*15, 'Travel Expenses', '-' *16)
print(f'{"Location:":<30}{destination}')
print(f'{"Initial Budget:":<30}${budget:.2f}')
print(f'{"Fuel:":<30}${fuel:.2f}')
print(f'{"Accomodation:":<30}${hotel:.2f}')
print(f'{"Food:":<30}${food:.2f}')
expenses = fuel + hotel + food
remaining_balance = budget - expenses
print('-'*48)
print(f'\n{"Remaining Balance:":<30}${remaining_balance:.2f}')


