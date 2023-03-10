from bs4 import BeautifulSoup
import requests
import pandas as pd

# get data from website as a soup object
def get_soup(url) -> BeautifulSoup:
    try:
        page = requests.get(url)
        if page.status_code == 200:
            return BeautifulSoup(page.content, 'html5lib')
        else:
            print("Error:", page.status_code)
    except Exception as e:
        print("Error:", e)

# get the list of items from the soup object
def collect_items(soup) -> list:
    try:
        items = soup.find_all('div', class_='_1xHGtK _373qXS')
        if len(items) > 0:
            return items
    except Exception as e:
        print("Error:", e)
        

# extract data and return a dictionary
def extract_data(item) -> dict:
    try: brand = item.find('div', class_='_2WkVRV')
    except: brand = None

    try: product = item.find('a', class_='IRpwTa _2-ICcC')
    except: product = None
    
    try: link = item.find('a', class_='IRpwTa').attrs.get('href')
    except: link = None
        try:

    try: price = item.find('div', class_='_30jeq3')
    except: price = None

    try: discount = item.find('div', class_='_3Ay6Sb')
    except: discount = None

    data = {
        'brand': item.find('div', class_="")
    }

# save the data to a csv file
def save_data(data, filename):
    pass

# main function to run the program
def main():
    s = 'bags'
    url = f'https://www.flipkart.com/search?q={s}'
    print('URL =>', url)
    soup = get_soup(url)
    items = collect_items(soup)
    if isinstance(items, list):
        print(f"Total items found: {len(items)}")

# call the function
main()