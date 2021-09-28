import bs4
from bs4 import BeautifulSoup
import requests
import csv

pageURL = 'https://en.wikipedia.org/wiki/Game_(hunting)'

page = requests.get(pageURL)
soup = BeautifulSoup(page.content, 'lxml')

articleBody = soup.find('div', {'class' : 'mw-parser-output'})

with open('List_of_game_animals.csv', 'w', newline='') as outputFile:
    for item in articleBody.find_all('ul'):
        outputFile.write(item.text + '\n')
outputFile.close()