from json_object import JsonClass
import re


class GetInfoFromJson:
    LINK_PATTERN = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'

    def __init__(self):
        self.json_class = JsonClass()

    def get_info_about_ship(self, *data, link, dictionary) -> dict:
        json_file = self.json_class.get_json(link)
        dictionary_list = []
        for i in data:
            for j in json_file:
                if i == j and isinstance(json_file.get(j), list):
                    for url in json_file.get(j):
                        if re.match(self.LINK_PATTERN, url):
                            pilots = self.get_info_about_pilots('name', 'height', 'mass', 'homeworld', link=url,
                                                           lst=dictionary_list)
                    dictionary.update({j: pilots})
                elif i == j:
                    dictionary.update({j: json_file.get(j)})
                    break
        return dictionary

    def get_info_about_pilots(self, *data, link, lst) -> list:
        dictionary = {}
        json_file = self.json_class.get_json(link)
        for i in data:
            for j in json_file:
                if i == j and re.match(self.LINK_PATTERN, json_file.get(j)):
                    dictionary.update({j: json_file.get(j)})
                    self.get_info_about_planet('homeworld_name', json_file.get(j), dictionary)
                    break
                elif i == j:
                    dictionary.update({j: json_file.get(j)})
                    break
        lst.append(dictionary)
        return lst

    def get_info_about_planet(self, name, link, dictionary):
        json_file = self.json_class.get_json(link)
        dictionary.update({name: json_file.get('name')})