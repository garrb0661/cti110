# Barbara Garr
# 5 December 24
# P4HW2
# This program calculates the pay of employees based on input from the user.

# Enter employee name or Done
# Enter number of hours worked as an interger
# Enter employee's pay rate as a float
# Calculate overtime_pay_rate = pay_rate * 1.5

employee_name = input("Enter employee's name or \'Done\' to terminate: ")
# create increment for employee count using 'employee_total +=1'
# create incremental sums for pay totals using '+='
overtimePay_total = 0.0
regPay_total = 0.0
grossPay_total = 0.0
employee_total = 0

while employee_name != 'Done':
    employee_total +=1
    hours_worked = int(input(f"How many hours did {employee_name} work: "))
    pay_rate = float(input("Enter emploee's pay rate: "))
    overtimePay_rate = pay_rate * 1.5

    # Enter if statements to determine overtime hours.
    # If hours_worked is greater than 40, then overtime_hours = hours_worked - 40
    # If hours_worked is less than or equal to 40, then overtime_hours = 0

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
    else:
        overtime_hours = 0

    # Calculate reg_pay_hours = hours_worked - overtime_hours 
    # Calculate reg_pay = reg_pay_hours * pay_rate
    # Calculate overtime_pay = overtime_hours * overtime_pay_rate
    # Calculate gross_pay = overtime_pay + reg_pay

    regPay_hours = hours_worked - overtime_hours
    regPay = regPay_hours * pay_rate
    regPay_total += regPay
    overtimePay = overtime_hours * overtimePay_rate
    overtimePay_total += overtimePay
    grossPay = overtimePay + regPay
    grossPay_total += grossPay

    # Display "-" * 40
    # Display "Employee name: ", employee_name
    # Display an empty line with print()
    # Print f'{"Hours Worked":<15}{"Pay Rate":<13}{"Overtime":<13}'
    #      f'{"OverTime Pay":<17}{"RegHour Pay":<15}{"Gross Pay":<15}')
    # Display "-" * 85
    # Print f'{hours_worked:<15.1f}${pay_rate:<12.2f}{overtime_hours:<13.1f}'
    #      f'${overtime_pay:<16.2f}${reg_pay:<14.2f}${gross_pay:<15.2f}')
    # This provides spacing and floating point values as needed
    # Enter employee name or Done
    
    print("-" * 40)
    print("Employee name: ", employee_name)
    print()
    print(f'{"Hours Worked":<15}{"Pay Rate":<13}{"Overtime":<13}'
        f'{"OverTime Pay":<17}{"RegHour Pay":<15}{"Gross Pay":<15}')
    print("-" * 85)
    print(f'{hours_worked:<15.1f}${pay_rate:<12.2f}{overtime_hours:<13.1f}'
        f'${overtimePay:<16.2f}${regPay:<14.2f}${grossPay:<15.2f}')
    employee_name = input("Enter employee's name or \'Done\' to terminate: ")


# display overtime total, regular pay total, gross pay total, total employees
print(f"\nTotal number of employees entered: {employee_total}")
print(f"Total amount paid for overtime: ${overtimePay_total}")
print(f"Total amount paid for regular hours: ${regPay_total}")
print(f"Total amount paid in gross: ${grossPay_total}")


