from house import House


class Human:
    default_name = 'Dima'
    default_age = 25

    def __init__(self, money: int, house: bool, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        print(f'Name --> {self.name} \nAge --> {self.age} \nMoney --> {self.__money} \nHouse --> {self.__house}')

    @staticmethod
    def default_info():
        print(f'Default name --> {Human.default_name} \nDefault age --> {Human.default_age}')

    def __make_deal(self, house: House, price):
        self.__money -= price
        self.__house = house
        print(f'Congratulations!!! You have just bought new small house!')
        return self.__house

    def earn_money(self, salary):
        self.__money += salary
        return self.__money

    def buy_house(self, house: House, discount):
        price_with_discount = house.final_price(discount)
        if price_with_discount <= self.__money:
            self.__make_deal(house, price_with_discount)
        else:
            print(f"You haven't enough money to buy this house")
