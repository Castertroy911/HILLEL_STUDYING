programming_languages = ['Python', 'Java', 'C++', 'Ruby']
authors = ['Guido van Rossum', 'James Gosling', 'Bjarne Stroustrup', 'Yukihiro Matsumoto']

# Сделал здесь dictionary comprehension чтобы потренироваться

languages_and_authors = {key: value for key, value in zip(programming_languages, authors)}

for key, value in languages_and_authors.items():
    print(f'My favorite programming language is {key}. It was created by {value}..')



# --------------------------------------------------------------
del languages_and_authors['Java']
print(f'Dictionary without Java: \n\t\t\t\t {languages_and_authors}')
