import requests
from datetime import datetime
from bs4 import BeautifulSoup
import os

BASE_DIR = os.path.dirname(os.path.abspath('__FILE__'))

def worldwideboxoffice(year=datetime.now().year):

    fname = f"box-office-{year}.csv"

    fdir = os.path.join(BASE_DIR, fname)

    file = open(fname, 'w')
    url = 'https://www.boxofficemojo.com/year/world/{}/'.format(year)
    response = requests.get(url)

    if response.status_code == 200:
        markup = response.text
        soup = BeautifulSoup(markup, features="html.parser")
        tr = soup.find_all('tr')
        for e in tr:
            for td in e:
                file.write(td.text.strip().replace(',','')+",")
            file.write('\n')


if __name__ == "__main__":
    worldwideboxoffice()
