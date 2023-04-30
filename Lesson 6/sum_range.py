def sum_range(start, stop):
    sum_value = 0
    if start < stop:
        for i in range(start, stop + 1):
            sum_value += i
    else:
        for i in range(stop, start + 1):
            sum_value += i
    return sum_value


if __name__ == '__main__':
    start_value = int(input('Please, enter the "start" value: '))
    stop_value = int(input('Please, enter the "stop" value: '))

    print(sum_range(start_value, stop_value))
