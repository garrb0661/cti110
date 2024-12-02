# Barbara Garr
# 19 November 24
# P2HW2
# This program takes a number grade and determines average

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# determine lowest, highest, sum, and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = sum(grades) / len(grades)

# display "-----------Results------------"
# display "Lowest Grade:", low. Low floating point value is 1.
# display "Highest Grade:", high. High floating point value is 1.
# display "Sum of Grades:", total. Total floating point value is 1.
# display "Average:", avg. Avg floating point value is 2.
# display "------------------------------------------"

print()
print('-----------Results------------')
print(f'{"Lowest Grade:":<20}{low:.1f}')
print(f'{"Highest Grade:":<20}{high:.1f}')
print(f'{"Sum of Grades:":<20}{total:.1f}')
print(f'{"Average:":<20}{avg:.2f}')
print('------------------------------------------')
