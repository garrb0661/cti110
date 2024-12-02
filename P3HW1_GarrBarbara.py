# Barbara Garr
# 26 November 24
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# determine lowest, highest , sum, and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = sum(grades) / len(grades)

# display "-" * 10, "Results", "-" * 10
# display "Lowest Grade:", low. Low floating point value is 1.
# display "Highest Grade:", high. High floating point value is 1.
# display "Sum of Grades:", total. Total floating point value is 1.
# display "Average:", avg. Avg floating point value is 2.
# display "-" * 40

print()
print('-'*10, 'Results', '-' *10)
print(f'{"Lowest Grade:":<20}{low:.1f}')
print(f'{"Highest Grade:":<20}{high:.1f}')
print(f'{"Sum of Grades:":<20}{total:.1f}')
print(f'{"Average:":<20}{avg:.2f}')
print('-'*40)

# determine letter grade for average using elif 

if avg >= 90:
    print('Your grade is: A')   
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')

    
# another option to determine letter grade using if/else
'''
if avg >= 90:
    print('Your grade is: A')
else:
    if avg >= 80:
        print('Your grade is: B')
    else:
        if avg >= 70:
            print('Your grade is: C')
        else:
            if avg >= 60:
                print('Your grade is: D')
            else:
                if avg < 60:
                    print('Your grade is: F')
'''   





