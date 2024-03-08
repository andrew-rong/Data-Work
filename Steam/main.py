import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


def get_reviews(app_id):
    params = {'json': 1}
    url = 'https://store.steampowered.com/appreviews/'
    response = requests.get(url=url + app_id, params=params)
    return response.json()


def get_n_reviews(app_id, n=100):
    reviews = []
    cursor = '*'
    params = {
        'json': 1,
        'language': 'english',
        'day_range': 365,
        'purchase_type': 'all',
        'num_per_page': '100'
    }
    while True:
        params['cursor'] = cursor.encode()
        params['num_per_page'] = n

        response = get_reviews(app_id)  # Getting reviews
        cursor = response['cursor']  # The next cursor value for the next batch
        reviews += response['reviews']  # Appending reviews

        if len(reviews) == 1000:
            break

    return reviews


x = get_reviews('1593500')

print(x["query_summary"])
summary = json.loads(str(x["query_summary"]))
# data = pd.json_normalize(x, 'reviews')

summary.to_csv("Summary.csv")
# data.to_csv("Data.csv")
