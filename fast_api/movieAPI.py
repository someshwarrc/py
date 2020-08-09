import os
import sys
import csv

BASE_DIR = os.path.dirname(os.path.abspath("__FILE__"))
WEB_SCRP = os.path.join(os.path.dirname(BASE_DIR), "web_scraping")

sys.path.insert(1, WEB_SCRP) # for importing another file from a different directory

import webscrape2csv
from fastapi import FastAPI

app = FastAPI()

async def get_movie_json(year=None):
    csv_str = webscrape2csv.worldwideboxoffice(year=year).rstrip()
    lines = csv_str.split('\n')
    labels = [e.replace("\"","") for e in lines[0].split(',')]

    # as a dictionary cannot have same key names
    labels[-1] = 'Foreign%'
    labels[-3] = 'Domestic%'

    movies = []
    for row in lines:
        movie = {}
        for i, val in enumerate([e.replace("\"","") for e in row.split("\",\"")]):
            movie[labels[i]] = val
        movies.append(movie)

    return movies

@app.get('/')
def home():
    return {"msg": "Welcome to the API service. Use /<year> to get the data as json."}

@app.get('/{year}')
async def year(year: int):
    movies = await get_movie_json(year)
    return movies
