# Можно было сделать более интересное решение

# word = list(input('Please, enter the word: '))
# first = 0
# last = len(word) - 1
# palindrom = True
# while first < last:
#     if word[first] != word[last]:
#         print('-')
#         palindrom = False
#         break
#     else:
#         first += 1
#         last -= 1
# if palindrom:
#     print('+')


word = input('Please, enter the word: ')
print('+') if word == word[::-1] else print('-')
