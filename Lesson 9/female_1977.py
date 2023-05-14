import json
final_result = {'count': 0}


def females_after_1977(json_file, dictionary: dict) -> str:
    with open(json_file) as file:
        json_data = json.load(file)
        for data in json_data:
            counter = 0
            for _ in data:
                value = data.get(_)
                if isinstance(value, list):
                    for j in value:
                        if j['gender'] == 'Female' and j['year'] > 1977:
                            counter += 1
            if dictionary.get('count') < counter:
                dictionary.update({'id_group': data.get('id_group')})
                dictionary.update({'count': counter})
    return f'Group id --> {dictionary.get("id_group")} ' \
           f'\nFemales after 1977 year of birth --> {dictionary.get("count")}'
