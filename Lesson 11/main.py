from small_house import Human, SmallHouse

if __name__ == '__main__':
    Human.default_info()
    human = Human(1000, True)
    human.info()
    small_house = SmallHouse(2000)
    human.buy_house(small_house, 10)
    human.earn_money(1200)
    human.buy_house(small_house, 10)
