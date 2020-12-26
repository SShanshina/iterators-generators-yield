import requests
import json
from tqdm import tqdm


class CountryLinks:

    def __init__(self, file_name):
        self.file_name = file_name
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):

        with open(self.file_name) as file:
            data = json.load(file)

        self.counter += 1

        while self.counter < len(data):
            country = data[self.counter]['name']['official']
            response = requests.get(
                        'http://wikipedia.org/w/api.php',
                        params={
                            'action': 'opensearch',
                            'search': {country},
                            'inprop': 'url'
                        })
            url_list = response.json()[3]
            if len(url_list) > 0:
                url = url_list[0]
            else:
                url = 'This page does not exist'
            return f'{country}: {url}'

        else:
            raise StopIteration


if __name__ == '__main__':
    with open('countries.txt', 'w', encoding='utf-8') as f:
        for country_link in tqdm(CountryLinks('countries.json')):
            f.write(f'{country_link}\n')
