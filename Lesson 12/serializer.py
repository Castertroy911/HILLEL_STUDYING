import json


class Serializer:
    def serialize_to_json(self, file_name, data: dict):
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)