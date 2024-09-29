from bs4 import BeautifulSoup
import csv
import re
import requests


URLS = [
    'https://www.myminifactory.com/collection/fetch-collection-objects/2101472',
    'https://www.myminifactory.com/collection/fetch-collection-objects/2101569',
]
PRICE_PATTERN = r'\d+\.\d{2}'
INFO = []

def make_request(url):
    page = requests.get(url)

    if page.status_code == 200:
        return page.content
    else:
        print(f"Status Code: {page.status_code}")


def get_links(page):
    soup = BeautifulSoup(page, 'lxml')

    return soup.find_all('a', {'class': 'searchtitle searchtext searchtitle-store'})


def parse_link_element(link):
# <a target="_blank" title="Modular Swords for hire : Halfling Elite [PRE-SUPPORTED]" href="/object/3d-print-modular-swords-for-hire-halfling-elite-pre-supported-386546" class="searchtitle searchtext searchtitle-store ">
#   <i class="fa fa-usd" aria-hidden="true" title="On sale"></i>
#   <span title="On sale">12.00 - </span> Modular Swords for hire : Halfling Elite [PRE-SUPPORTED]
# </a>
    return [
        link.attrs['title'],
        get_price(link.text.strip()),
        'https://www.myminifactory.com' + link.attrs['href'],
    ]


def get_price(text):
    match = re.search(PRICE_PATTERN, text)

    if match:
        return match.group()
    else:
        return ''


if __name__ == '__main__':
    for url in URLS:
        page = make_request(url)
        links = get_links(page)

        for link in links:
            INFO.append(parse_link_element(link))

    for info in INFO:
        print(info)
