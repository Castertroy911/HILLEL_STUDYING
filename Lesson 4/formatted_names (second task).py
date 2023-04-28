names = ["John", "Marta", "James", "Amanda", "Marianna"]

'''
Если честно - то я сначала подумал, что нужно выровнять по правому краю немного по другому и решил сделать так: сначала
я узнавал максимальную длину слова в списке, затем подставлял это значение в метод .rjust(width) и таким образом
выравнивал по правому краю. Но потом, почитав заданиче, почему-то решил, что нужно сделать иначе и поэтому здесь
только последние две строки кода. Но на всякий случай оставил и первый вариант решения.
'''

# width = 0
# for name in names:
#     if len(name) > width:
#         width = len(name)

for name in names:
    print(f'{"NAME".center(50, "*")} \n {name.rjust(49)}')
