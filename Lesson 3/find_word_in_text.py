text = input('Please, enter the text: ').lower().split()
word = input('Please, enter the word: ').lower()

# Можно сделать через тернарный оператор
# print('YES') if word in text and len(text) > 0 else print('NO')


# Но мне кажется более удобнм и читаемым вариант в несколько строк

if word in text and len(text) > 0:
    print('YES')
else:
    print('NO')
