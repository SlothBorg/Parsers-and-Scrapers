import bs4
from bs4 import BeautifulSoup
import requests
import csv

baseURL = 'http://www.innatthecrossroads.com/home/game-thrones-recipes/recipes-by-meal/'
pages = [
    'main-courses',
    'sides',
    'breakfast',
    'soupsstews',
    'pies',
    'bread',
    'vegetarian',
    'desserts',
    'beverages',
]
outputFile = open('Game of Thrones', 'w')
for page in pages:
    page = requests.get(baseURL + page)
    soup = BeautifulSoup(page.content, 'lxml')
    menus = soup.find('article')
    for item in menus.find_all('li'):
        outputFile.write(item.text + '\n')

outputFile.close()