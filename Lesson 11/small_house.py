from human import Human, House


class SmallHouse(House):
    def __init__(self, price, area=40):
        super().__init__(area, price)
        self.area = area
