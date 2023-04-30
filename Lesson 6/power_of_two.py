import math


def power_of_two(number):
    log = int(math.log2(number))
    if 2 ** log == number:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    err = True
    while err:
        try:
            entered_number = int(input('Please, enter the number: '))
            err = False
        except ValueError:
            print('You need to enter only number, not letters or symbols!')
            err = True

    print(power_of_two(entered_number))
