import bs4
from bs4 import BeautifulSoup
import requests
import csv

baseURL = 'http://www.sfwa.org'
pageURL = '/2009/08/fantasy-worldbuilding-questions/'
page = requests.get(baseURL + pageURL)
soup = BeautifulSoup(page.content, 'lxml')
bodyDiv = soup.find('div', {'class' : 'body'})
with open('links.csv', 'w', newline='') as csvfile:
    rowWriter = csv.writer(csvfile, delimiter='\t')
    for link in bodyDiv.find('ul'):
        if type(link) is not bs4.element.NavigableString:
            for item in link:
                if item.name == 'a':
                    rowWriter.writerow([item['href'].strip()])