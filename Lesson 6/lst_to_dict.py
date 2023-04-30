entered_list = input('Please, enter the list of any values: ').split()


# Я видел, что по условиям задания предполагается, что список будет содержать валидные значения для создания
# словаря, но все же решил перестраховаться и преобразовать полученный словарь в set(), чтобы убрать дубликаты
def to_dict(lst):
    working_lst = set(lst)
    dictionary = {}
    for i in working_lst:
        dictionary[i] = i
    return dictionary
