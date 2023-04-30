def change_list(lst):
    if len(lst) >= 2:
        first_element = lst[0]
        lst[0] = lst[-1]
        lst[-1] = first_element
        return lst
    else:
        return print('List contains less than 2 elements!')


if __name__ == '__main__':
    entered_list = input('Please, enter the list of any values: ').split()

    print(change_list(entered_list))
