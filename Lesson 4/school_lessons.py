subjects = {'science': {'physics': ['nuclear physics', 'optics', 'thermodynamics'],
                        'computer science': {}, 'biology': {}}, 'humanities': {}, 'public': {}}

number = 1
for keys in subjects['science'].keys():
    print(f"The subjects['science'] key number {number} --> {keys}")
    number += 1

print(f'Values of the "subjects[\'science\'][\'physics\']": {subjects["science"]["physics"]}')