import datetime


def function_result_in_file(func):
    def wrapper(*args):
        result = func(*args)
        with open('result_file.txt', 'w+') as file:
            launch_time = datetime.datetime.now().time()
            file.write(f'Function launched at {launch_time.strftime("%H:%M:%S")} with result {result}')
    return wrapper


@function_result_in_file
def sum_func(*args: int):
    result = sum(args)
    return result
