class Dot:
    x = None
    y = None

    def dot(self):
        self.x, self.y = [int(i) for i in input(f'Please, enter "x" and "y" values.').split()]
        return self.x, self.y

    def get_dot(self):
        x, y = self.dot()
        return x, y

    @staticmethod
    def length_of_line(x1, y1, x2, y2):
        length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return length

    @staticmethod
    def is_triangle_coordinates_are_valid(x1, y1, x2, y2, x3, y3):
        if (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3) == 0:
            return False
        return True


class Triangle:
    def __init__(self):
        self.dot = Dot()

    def square_of_triangle(self):
        a = self.dot.get_dot()
        b = self.dot.get_dot()
        c = self.dot.get_dot()
        if self.dot.is_triangle_coordinates_are_valid(*a, *b, *c):
            a_b = self.dot.length_of_line(*a, *b)
            b_c = self.dot.length_of_line(*b, *c)
            a_c = self.dot.length_of_line(*a, *c)
            p = (a_b + b_c + a_c) / 2
            square = (p*(p - a_b)*(p - b_c)*(p - a_c)) ** 0.5
            square = round(square, 1)
            return square
        raise Exception(f'Coordinates are not valid!!!')


class Quadrate:
    def __init__(self):
        self.dot = Dot()

    def square_of_quadrate(self):
        a = self.dot.get_dot()
        b = self.dot.get_dot()
        c = self.dot.get_dot()
        d = self.dot.get_dot()
        if self.dot.is_triangle_coordinates_are_valid(*a, *b, *c) and self.dot.is_triangle_coordinates_are_valid(*a, *b, *d) and self.dot.is_triangle_coordinates_are_valid(*a, *c, *d) and self.dot.is_triangle_coordinates_are_valid(*b, *c, *d):
            a_b = self.dot.length_of_line(*a, *b)
            square = a_b ** 2
            return square
        raise Exception(f'Coordinates are not valid!!!')



if __name__ == "__main__":
    quadrate = Quadrate()
    print(quadrate.square_of_quadrate())

    triangle = Triangle()
    print(triangle.square_of_triangle())

