v1 = int(input('Please, enter first water value: '))
t1 = int(input('Please, enter first water temperature: '))
v2 = int(input('Please, enter second water value: '))
t2 = int(input('Please, enter second water temperature: '))

if v1 == 0 and v2 == 0:
    print('Enter not zero value for "first water value" or "second water value": ')
    v1 = int(input('Please, enter not zero first water value: '))
    v2 = int(input('Please, enter not zero second water value: '))
    volume_and_temperature = (v1 * t1 + v2 * t2) / (v1 + v2)
    print(f'Volume and temperature is {round(volume_and_temperature, 2)}')
else:
    volume_and_temperature = (v1 * t1 + v2 * t2) / (v1 + v2)
    print(f'Volume and temperature is {round(volume_and_temperature, 2)}')