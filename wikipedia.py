import requests
import json
from tqdm import tqdm


class WikiIter:

    def __init__(self, country_name):
        self.country_name = country_name
        self.response = requests.get(
            'http://wikipedia.org/w/api.php',
            params={
                'action': 'opensearch',
                'search': {self.country_name},
                'inprop': 'url'
            })

    def __iter__(self):
        return self

    def __next__(self):
        while self.country_name:
            url = self.response.json()[3]
            return url
        else:
            raise StopIteration


if __name__ == '__main__':
    with open('countries.json') as file:
        data = json.load(file)
    countries = []
    for country in data:
        country_name = country['name']['official']
        countries.append(country_name)
    with open('countries.txt', 'w', encoding='utf-8') as f:
        for country in tqdm(countries):
            wiki_url = WikiIter(country)
            if len(next(wiki_url)) > 0:
                url = next(wiki_url)[0]
                f.write(f'{country}: {url}\n')
            else:
                f.write(f'{country}: This page does not exist\n')
