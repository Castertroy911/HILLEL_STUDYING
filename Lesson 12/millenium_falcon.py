from get_info_from_json import GetInfoFromJson
from serializer import Serializer
from pprint import pprint

if __name__ == '__main__':
    get_info = GetInfoFromJson()
    serializer = Serializer()
    info_dict = {}

    get_info.get_info_about_ship("name", "max_atmosphering_speed", "starship_class", "pilots",
                        link='https://swapi.dev/api/starships/10/', dictionary=info_dict)
    serializer.serialize_to_json('millenium falcon.json', info_dict)

    pprint(info_dict)
