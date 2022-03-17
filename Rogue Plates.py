import time
import requests
from bs4 import BeautifulSoup

url = "https://www.roguecanada.ca/rogue-mil-echo-bumper-plates-black"
# url = "https://www.roguecanada.ca/rogue-color-lb-training-2-0-plates"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('div', class_="normal view-all")
#print(results.prettify())

packages = results.find_all('div', class_='rhpa-opts option grouped-rhpa')
individuals = results.find_all('div', class_='rhpa-opts option grouped-rhpa hide-more')

for elem in packages:
    name_elem = elem.find('div', class_='simple-name').text
    price_outer_class = elem.find('div', class_='product-price simple-price rhpa-child condensed').text
    print(name_elem, price_outer_class)

for elem in individuals:
    name_elem = elem.find('div', class_='simple-name').text
    price_outer_class = elem.find('div', class_='product-price simple-price rhpa-child condensed').text
    print(name_elem, price_outer_class)

# Updated the site so this no longer works :(
# Plus i don't have a reference for what out of stock is now that everythings in stock...
"""
for elem in prod_elems:
    name_elem = elem.find('div', class_='item-name')
    price_elem = elem.find('span', class_='price')
    # availability is none if there is no out of stock button for the packages, in the function .text
    # Problem here,
    # if the plates are out of stock individually, then site doesn't say out of stock
    # instead it states a new block saying notify me
    if elem.find('div', class_='bin-out-of-stock-message bin-out-of-stock-default') is None:
        if elem.find('button', class_='v-btn'):
            availability = "Out of stock"
        else:
            availability = "In Stock"
    else:
        availability = elem.find('div', class_='bin-out-of-stock-message bin-out-of-stock-default').text

    print(name_elem.text, price_elem.text, availability)
    # the values are tags by themselves with .text it becomes strings so this can be used

"""