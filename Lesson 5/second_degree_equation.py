# Создал свой ексепшн по примеру их лекции
class DiscriminantError(Exception):
    pass


# Зациклил ввод данных до тех пор, пока не будет введены только числа
try:
    a, b, c = (int(i) for i in input('Please, enter numbers: ').split())
    err = False
except ValueError:
    err = True
    while err:
        try:
            a, b, c = (int(i) for i in input('Please, enter only numbers: ').split())
            err = False
        except ValueError:
            err = True

DISCRIMINANT = b ** 2 - 4 * a * c


# Пара функций, чтобы не использовать повторно одинаковые формулы
def first_x(a, b):
    x_1 = (-b + DISCRIMINANT ** 0.5) / (2 * a)
    return x_1


def second_x(a, b):
    x_2 = (-b - DISCRIMINANT ** 0.5) / (2 * a)
    return x_2


# Реализация задания 
if DISCRIMINANT > 0 and a != 0:
    print(f'x1 = {int(first_x(a, b))}')
    print(f'x2 = {int(second_x(a, b))}')
elif DISCRIMINANT == 0:
    print(f'x = {int(first_x(a, b))}')
else:
    raise DiscriminantError(f'Discriminant < 0, so there are no correct answers')
