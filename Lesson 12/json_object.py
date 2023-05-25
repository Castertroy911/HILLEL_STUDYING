import requests


class JsonClass:
    BASE_URL = 'https://swapi.dev/api/'

    def get_endpoint(self, base_url: str, full_url: str):
        endpoint = full_url.replace(base_url, '/')
        return endpoint

    def get_json(self, url):
        result = requests.get(self.BASE_URL + self.get_endpoint(self.BASE_URL, url))
        result = result.json()
        return result
