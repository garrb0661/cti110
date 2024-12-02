# Barbara Garr
# 13 November 24
# P1HW1
# A program to calculate exponents along with addition and subtraction.

print('-----Caluculating Exponents-----')
base_value = int(input('Enter an interger as the base value: '))
exponent = int(input('Enter an interger as the exponent: '))
total = base_value ** exponent
print('\n', base_value, 'raised to the power of', exponent, 'is', total, '!!')

print('\n-----Addition and Subtraction-----')
starting_interger = int(input('Enter a starting interger: '))
add = int(input('Enter an interger to add: '))
subtract = int(input('Enter an interger to subtract: '))
total = int(starting_interger + add - subtract)
print('\n', starting_interger, '+', add, '-', subtract, 'is equal to', total)
