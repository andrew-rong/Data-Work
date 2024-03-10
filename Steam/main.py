import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pickle
import nltk
from nltk import FreqDist


# nltk.download("punkt")
# nltk.download("stopwords")
# nltk.download('averaged_perceptron_tagger')
# nltk.download('tagsets')


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


# x = get_reviews('1593500')

def store_reviews(csv):
    pass
# summary = json.dumps(x["query_summary"])
# data = pd.json_normalize(x, 'reviews')

# summary.to_csv("Summary.csv")
# data.to_csv("Data.csv")

# with open('summary.pkl', 'wb') as f:
#     pickle.dump(summary, f)

# with open('summary.pkl', 'rb') as f:
#     loaded_dict = pickle.load(f)


data = pd.read_csv('Data.csv')
# print(data["review"][6])
trial = data["review"][6]

tokens = word_tokenize(trial)
print(tokens)

# Filtering stop words
stop_words = set(stopwords.words("english"))

filtered_list = [word for word in tokens if word.casefold() not in stop_words]

# Stemming
stemmer = PorterStemmer()

# Targeting
#type_of_word = nltk.pos_tag(filtered_list)

# print(type_of_word)

frequency_distribution = FreqDist(filtered_list)
# print(frequency_distribution)
frequency_distribution.plot(20, cumulative=True)
