def square(value):
    perimeter = value * 4
    square_area = value ** 2
    diagonal = 2 ** 0.5 * value
    return perimeter, square_area, diagonal


if __name__ == '__main__':
    err = True
    while err:
        try:
            entered_value = int(input('Please, enter the number value: '))
            err = False
        except ValueError:
            print('You need to enter only number, not letters or symbols!')
            err = True

    print(square(entered_value))
