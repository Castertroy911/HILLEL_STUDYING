text = input('Please, enter the text: ').split()

if len(text) >= 3:
    print(*text[-3:])
else:
    print(f'There is only {len(text)} element(s) in the text')
