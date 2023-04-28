camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]

'''
В первом цикле for использовал enumerat(), чтобы получить индекс элемента из списка camel_case_list. Потом использовал
этот индекс, чтобы заменить элемент в КемелКейс, на элемент в снейк_кейс (строка 13). Можно было бы сделать чуть проще,
создать новый список и просто в него через .append() добавлять измененные элементы, но это бы заняло дополнительную
память.
'''
for index, word in enumerate(camel_case_list):
    for index_1, value in enumerate(word):
        if index_1 > 0 and value.isupper():
            snake_case = word.replace(word[index_1], f'_{value}').lower()
            camel_case_list[index] = snake_case
print(f'List in snake_case: {camel_case_list}')
