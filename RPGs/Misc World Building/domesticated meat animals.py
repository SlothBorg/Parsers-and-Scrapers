import bs4
from bs4 import BeautifulSoup
import requests
import csv

pageURL = 'https://en.wikipedia.org/wiki/List_of_domesticated_meat_animals'

page = requests.get(pageURL)
soup = BeautifulSoup(page.content, 'lxml')
articleBody = soup.find('table', attrs={'style' : "width:100%;"})
table = articleBody.find_all('td')
for tableData in table:
    print(tableData.find('ul'))
    print('--------------------------')

# listOfAnimals = []
# for item in articleBody.find_all('td'):
#     print(item)



# with open('List_of_domesticated_meat_animals.csv', 'w', newline='') as csvfile:
#     page = requests.get(pageURL)
#     soup = BeautifulSoup(page.content, 'lxml')
#     menus = soup.find('div', {'class' : 'mw-parser-output'})
#     for item in menus.find_all('li'):
#         outputFile.write(item.text + '\n')

# outputFile.close()