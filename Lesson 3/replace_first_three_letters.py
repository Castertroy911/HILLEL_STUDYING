string = input('Please, enter the word: ').lower()


# В задании было сказано только "заменить", но я на всякий случай еще и выводил измененные строки

if string[:3] == 'abc':
    string = string.replace(string[:3], 'www')
    print(string)
else:
    string += 'zzz'
    print(string)
