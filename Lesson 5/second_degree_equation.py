a, b, c = (int(i) for i in input().split())

DISCRIMINANT = b ** 2 - 4 * a * c


class DiscriminantError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


if DISCRIMINANT > 0 and a != 0:
    print(f'x1 = {(-b + DISCRIMINANT ** 0.5) / (2 * a)}')
    print(f'x2 = {(-b - DISCRIMINANT ** 0.5) / (2 * a)}')
elif DISCRIMINANT == 0:
    print(f'x = {(-b + DISCRIMINANT ** 0.5) / (2 * a)}')
else:
    raise DiscriminantError(f'Discriminant < 0, so there are no correct answers')
