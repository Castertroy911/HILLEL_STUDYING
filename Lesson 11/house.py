class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        price_with_discount = self._price - (self._price // 100 * discount)
        return price_with_discount
