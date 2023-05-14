import json
final_result = {'sum': 0}


def best_salesman(json_file, dictionary: dict) -> str:
    with open(json_file) as file:
        json_data = json.load(file)
        for data in json_data:
            for i in data:
                for j in data[i]:
                    sum_of_sales = 0
                    if j == 'first_name':
                        first_name = data[i][j]
                    elif j == 'last_name':
                        last_name = data[i][j]
                    elif i == 'cars':
                        for _ in data[i]:
                            sum_of_sales += _['price']
                if dictionary['sum'] < sum_of_sales:
                    dictionary.update({'first_name': first_name})
                    dictionary.update({'last_name': last_name})
                    dictionary.update({'sum': sum_of_sales})
    return f'Best salesman is {dictionary["first_name"]} {dictionary["last_name"]}' \
           f'\nHe sold cars on total sum ${dictionary["sum"]}'
