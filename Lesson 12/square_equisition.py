import argparse


class SquareEquisition:
    @staticmethod
    def __parse_data():
        parser = argparse.ArgumentParser()
        parser.add_argument('-a', type=int, default=0, help=
                            'This is parameter "a" of the second degree equation ax² + bx + c = 0')
        parser.add_argument('-b', type=int, help=
                            'This is parameter "b" of the second degree equation ax² + bx + c = 0')
        parser.add_argument('-c', type=int, help=
                            'This is parameter "b" of the second degree equation ax² + bx + c = 0')
        args = parser.parse_args()
        return args

    def __descriminant(self):
        data = self.__parse_data()
        return data.b ** 2 - 4 * data.a * data.c

    def __first_x(self):
        data = self.__parse_data()
        x_1 = (-data.b + self.__descriminant() ** 0.5) / (2 * data.a)
        return x_1

    def __second_x(self):
        data = self.__parse_data()
        x_2 = (-data.b - self.__descriminant() ** 0.5) / (2 * data.a)
        return x_2

    def square_equisition_result(self):
        data = self.__parse_data()
        if self.__descriminant() > 0 and data.a != 0:
            print(f'x1 = {int(self.__first_x())}')
            print(f'x2 = {int(self.__second_x())}')
        elif self.__descriminant() == 0:
            print(f'x = {int(self.__first_x())}')
        else:
            print(f'Discriminant < 0, so there are no correct answers')


if __name__ == '__main__':
    square_equisition = SquareEquisition()
    square_equisition.square_equisition_result()