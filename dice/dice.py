'''
Program will random number from 1 to 6 (numbers you can see on a dice).
Result will be printed on the screen as dice image.
'''

from random import randint

def dice(number):
    if number == 1:
        row1 = row3 = '   '
        row2 = ' o '
    elif number == 2 or number == 3:
        row1 = 'o  '
        row2 = '   '
        row3 = '  o'
        if number == 3:
            row2 = ' o '
    elif number == 4 or number == 5 or number == 6:
        row1 = row3 = 'o o'
        row2 = '   '
        if number == 5:
            row2 = ' o '
        elif number == 6:
            row2 = row1
    return '-' * 7 + f'\n| {row1} |\n| {row2} |\n| {row3} |\n' + '-' * 7

number1 = randint(1,6)
number2 = randint(1,6)
print(dice(number1))
print(dice(number2))
if number1 + number2 == 7:
    print('You WIN!')