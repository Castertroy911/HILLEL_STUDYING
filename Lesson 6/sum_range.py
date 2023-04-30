def sum_range(start, stop):
    sum_value = 0
    if start < stop:
        for i in range(start, stop + 1):
            sum_value += i
    else:
        for i in range(stop, start + 1):
            sum_value += i
    return sum_value
