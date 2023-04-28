english = ['stork', 'hawk', 'woodpecker', 'owl']
german = ['storch', 'falke', 'specht', 'eule']

e2g = {key: value for key, value in zip(english, german)}
print(f'Dictionary v1.0.0 --> {e2g}', end='\n\n')
print(f'"Owl" in German will be --> {e2g["owl"]}', end='\n\n')

e2g.update([('butterfly', 'schmetterlink'), ('pencil', 'kugelschreiber')])
print(f'Add new words in dictionary. Dictionary v1.0.1 --> {e2g}', end='\n\n')

for key, value in e2g.items():
    print(f'[{key},{value}]',end=', ') # условие задания "вывести отдельно: ключ и значение словаря в виде списков"
