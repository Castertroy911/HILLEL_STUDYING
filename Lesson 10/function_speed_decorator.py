import datetime


def function_speed(func):
    def wrapper(*args):
        start = datetime.datetime.now()
        func(*args)
        finish = datetime.datetime.now()
        print(finish - start)
    return wrapper


@function_speed
def long_func(value):
    counter = 0
    lst = []
    while counter != value:
        lst.append(counter)
        for i in lst:
            lst[lst.index(i)] = i ** 2
        counter += 1