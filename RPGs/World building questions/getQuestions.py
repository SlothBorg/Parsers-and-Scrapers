import bs4
from bs4 import BeautifulSoup
import requests
import csv

titlePrefix = 'Fantasy Worldbuilding Questions: '
listOfLinks = []
baseURL = 'http://www.sfwa.org'
listOfQuestions = []

# For Windows ugg, you need to use
# chcp 65001

with open('links.csv', 'r') as f:
    # reader = csv.reader(f)
    listOfLinks = list(csv.reader(f))

outputFile = open('Questions.txt', 'w', encoding='utf-8')
for link in listOfLinks:
    page = requests.get(baseURL + link[0])
    soup = BeautifulSoup(page.content, 'lxml')
    # print(soup.find('div', {'class' : 'body'}))
    pageTitle = soup.find('h2', {'class' : 'post_title'}).get_text().replace(titlePrefix, '')
    bodyDiv = soup.find('div', {'class' : 'body'})
    for item in bodyDiv.find('ol'):
        sectionTitle = ''
        if item.find('h3') != -1:
            sectionTitle = item.find('h3').get_text()
        if item.find('ul') != -1:
            for question in item.find('ul'):
                if question.name != None:
                    outputFile.write(pageTitle + '\t' + sectionTitle + '\t' + question.text + '\n')

outputFile.close()