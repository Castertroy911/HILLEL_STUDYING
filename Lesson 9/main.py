from best_salesman import best_salesman
from female_1977 import females_after_1977

if __name__ == '__main__':
    females_list = {'count': 0}
    the_best_salesman = {'sum': 0}
    print(females_after_1977('group_people.json', females_list))
    print(best_salesman('manager_sales.json', the_best_salesman))
