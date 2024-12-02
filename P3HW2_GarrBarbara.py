# Barbara Garr
# 29 November 24
# P3HW2
# This program calculates the pay of an employee based on input from the user.

# Enter employee name
# Enter number of hours worked as an interger
# Enter employee's pay rate as a float
# Calculate overtime_pay_rate = pay_rate * 1.5

employee_name = input("Enter employee's name: ")
hours_worked = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter emploee's pay rate: "))
overtime_pay_rate = pay_rate * 1.5

# Enter if statements to determine overtime hours.
# If hours_worked is greater than 40, then overtime_hours = hours_worked - 40
# If hours_worked is less than or equal to 40, then overtime_hours = 0

if hours_worked > 40:
    overtime_hours = hours_worked - 40
if hours_worked <= 40:
    overtime_hours = 0

# Calculate reg_pay_hours = hours_worked - overtime_hours 
# Calculate reg_pay = reg_pay_hours * pay_rate
# Calculate overtime_pay = overtime_hours * overtime_pay_rate
# Calculate gross_pay = overtime_pay + reg_pay

reg_pay_hours = hours_worked - overtime_hours
reg_pay = reg_pay_hours * pay_rate
overtime_pay = overtime_hours * overtime_pay_rate
gross_pay = overtime_pay + reg_pay
    
# Display "-" * 40
# Display "Employee name: ", employee_name
# Display an empty line with print()
# Print f'{"Hours Worked":<15}{"Pay Rate":<13}{"Overtime":<13}'
#      f'{"OverTime Pay":<17}{"RegHour Pay":<15}{"Gross Pay":<15}')
# Display "-" * 85
# Print f'{hours_worked:<15.1f}${pay_rate:<12.2f}{overtime_hours:<13.1f}'
#      f'${overtime_pay:<16.2f}${reg_pay:<14.2f}${gross_pay:<15.2f}')
# This provides spacing and floating point values as needed

print("-" * 40)
print("Employee name: ", employee_name)
print()
print(f'{"Hours Worked":<15}{"Pay Rate":<13}{"Overtime":<13}'
      f'{"OverTime Pay":<17}{"RegHour Pay":<15}{"Gross Pay":<15}')
print("-" * 85)
print(f'{hours_worked:<15.1f}${pay_rate:<12.2f}{overtime_hours:<13.1f}'
      f'${overtime_pay:<16.2f}${reg_pay:<14.2f}${gross_pay:<15.2f}')


