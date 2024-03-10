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
from nltk.sentiment import SentimentIntensityAnalyzer


# nltk.download("punkt")
# nltk.download("stopwords")
# nltk.download('averaged_perceptron_tagger')
# nltk.download('tagsets')
# nltk.download('state_union') this is some random dataset about WWII
# nltk.download('vader_lexicon')


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


def store_reviews(initial_data):
    summary = json.dumps(initial_data["query_summary"])
    reviews = pd.json_normalize(initial_data, 'reviews')
    summary.to_csv("Summary.csv")
    reviews.to_csv("Data.csv")
    with open('summary.pkl', 'wb') as f:
        pickle.dump(summary, f)
    with open('summary.pkl', 'rb') as f:
        loaded_dict = pickle.load(f)


# store_reviews(get_reviews('1593500'))


# Filtering stop words
def remove_stop_words(unfiltered_list):
    # Remove punctuation, for now unnecessary
    words = [w for w in unfiltered_list if w.isalpha()]
    stop_words = set(stopwords.words("english"))
    filtered_list = [word.lower() for word in words if word.casefold() not in stop_words]
    return filtered_list


"""data = pd.read_csv('Data.csv')
trial = data["review"][6]
tokens = word_tokenize(trial)
clean_words = remove_stop_words(tokens)"""


# frequency_distribution = FreqDist(clean_words)
# print(frequency_distribution.most_common(5))
# print(frequency_distribution.tabulate(3))    table form
# frequency_distribution.plot(5)


# text_type = nltk.Text(tokens)
# print(text_type.concordance("game", lines=5))
# Concordance must be of type nltk.Text
# Concordance displays sentences or words around the desired name


all_reviews = pd.read_csv("Reviews.csv", index_col=False)

# mass_test = []
# for i in all_reviews['review']:

sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores(all_reviews['review'][0]))
# print(all_reviews['review'][0])
