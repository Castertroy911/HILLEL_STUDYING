err = True
while err:
    try:
        entered_value = int(input('Please, enter the number value: '))
        err = False
    except ValueError:
        print('You need to enter only number, not letters or symbols!')
        err = True


def is_prime(value):
    for i in range(2, value + 1):
        if value % i == 0 and i != value:
            return False
        else:
            continue
    return True
