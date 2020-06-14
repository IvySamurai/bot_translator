import argparse
import requests
import lxml
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self):
        self.base_url = f'https://dictionary.cambridge.org/ru/словарь/англо-русский/'
        self.headers = {
            'accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }

    def get_translation(self, word):
        """ Gets a word translation """
        url = self.base_url + word
        with requests.Session() as session:
            try:
                response = session.get(url, headers=self.headers)
                soup = BeautifulSoup(response.text, 'lxml')
                translation = soup.find('span', attrs={
                    'class': 'trans dtrans dtrans-se'
                }).text
                return translation.strip()
            except AttributeError:
                return 'Некорректно введено слово. Попробуйте снова.'
