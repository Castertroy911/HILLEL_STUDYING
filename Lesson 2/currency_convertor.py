source_currency = input('Please, enter source currency: UAH, USD or EUR --> ')
target_currency = input('Please, enter target currency: UAH, USD or EUR --> ')
sum_of_money = int(input('Please, enter sum of money: '))

if source_currency.upper() == 'UAH' and target_currency.upper() == 'USD':
    usd_amount = sum_of_money / 37.45
    usd_amount = round(usd_amount, 2)
    print(f'₴{sum_of_money} --> ${usd_amount}')
elif source_currency.upper() == 'USD' and target_currency.upper() == 'UAH':
    uah_amount = sum_of_money * 36.57
    uah_amount = round(uah_amount, 2)
    print(f'${sum_of_money} --> ₴{uah_amount}')
elif source_currency.upper() == 'UAH' and target_currency.upper() == 'EUR':
    eur_amount = sum_of_money / 42
    eur_amount = round(eur_amount, 2)
    print(f'₴{sum_of_money} --> €{eur_amount}')
elif source_currency.upper() == 'EUR' and target_currency.upper() == 'UAH':
    uah_amount = sum_of_money * 40.42
    uah_amount = round(uah_amount, 2)
    print(f'€{sum_of_money} --> ₴{uah_amount}')
else:
    print('Please, doublecheck the entered currencies!!!')