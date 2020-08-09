import requests
from datetime import datetime
from bs4 import BeautifulSoup
import os

BASE_DIR = os.path.dirname(os.path.abspath('__FILE__'))

def worldwideboxoffice(year=datetime.now().year, csv=False):

    fname = f"box-office-{year}.csv"

    fdir = os.path.join(BASE_DIR, fname)

    file = open(fname, 'w')
    url = 'https://www.boxofficemojo.com/year/world/{}/'.format(year)
    response = requests.get(url)

    str = ""

    if response.status_code == 200:
        markup = response.text
        soup = BeautifulSoup(markup, features="html.parser")
        tr = soup.find_all('tr')
        for e in tr:
            for td in e:
                row = td.text.strip()
                row = "\""+ row +"\"" + ","
                # row = row[:-1] #removing last comma in the row
                str += row
            str = str[:-1]+'\n'
    
    if csv:
        file.write(str)

    file.close()
    return str


if __name__ == "__main__":
    str = worldwideboxoffice(2000, True)