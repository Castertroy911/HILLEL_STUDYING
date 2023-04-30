import math


err = True
while err:
    try:
        entered_number = int(input('Please, enter the number: '))
        err = False
    except ValueError:
        print('You need to enter only number, not letters or symbols!')
        err = True


def power_of_two(number):
    log = int(math.log2(number))
    if 2 ** log == number:
        print('Yes')
    else:
        print('No')
