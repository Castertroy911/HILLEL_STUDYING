def convert_to_usd_list_of_values(readed_file, coefficient):
    for i in readed_file:
        list_of_values = i.split(',')
        for j in list_of_values:
            try:
                amount_in_usd = int(j) * coefficient
                list_of_values[list_of_values.index(j)] = str(amount_in_usd)
            except ValueError:
                pass
        list_of_values.append('\n')
        converted_string = ','.join(list_of_values)
        readed_file[readed_file.index(i)] = converted_string
    return readed_file


if __name__ == '__main__':
    coefficient = 36.57
    with open('test_file.csv', 'r') as file:
        file_information = file.readlines()
        convert_to_usd_list_of_values(file_information, coefficient)

    with open('salaries_uah.csv', 'w') as file:
        file.writelines(file_information)
