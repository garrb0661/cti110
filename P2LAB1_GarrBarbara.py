# Barbara Garr
# 19 November 24
# P2LAB1
# This program calculates circle formulas.

# Pseudocode
# Import math function
# Ask user "What is the radius of a circle?"
# Input radius
# Set diameter = 2 * radius
# Display "The diameter of the circle is", diameter. Diameter floating-point value is 1
# Set circumference = 2 * math.pi * radius
# Display "The circumference of the circle is", circumference. Circumference floating-point value is 2
# Set area = math.pi * radius**2
# Display "The area of the circle is", area. Area floating-point value is 3

import math

radius = float(input('What is the radius of a circle? '))
diameter = 2 * radius
print('The diameter of the circle is', f'{diameter:.1f}')
circumference = 2 * math.pi * radius
print('The circumference of the circle is', f'{circumference:.2f}')
area = math.pi * radius**2
print('The area of the circle is', f'{area:.3f}')


