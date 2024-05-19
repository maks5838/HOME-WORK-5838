import requests
from bs4 import BeautifulSoup

base_url = 'http://books.toscrape.com/'

def get_book_titles(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.select('article.product_pod h3 a')
    titles = [book['title'] for book in books]

    return titles

def get_all_book_titles():
    titles = []
    url = base_url
    while True:
        titles.extend(get_book_titles(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        next_button = soup.select_one('li.next a')
        if next_button:
            next_page_url = next_button['href']
            url = base_url + next_page_url
        else:
            break

    return titles
all_titles = get_all_book_titles()
for title in all_titles:
    print(title)