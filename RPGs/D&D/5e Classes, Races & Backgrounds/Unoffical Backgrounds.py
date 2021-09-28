import bs4
from bs4 import BeautifulSoup
import csv
import requests

baseURL = 'http://engl393-dnd5th.wikia.com'
page = requests.get(baseURL + '/wiki/Backgrounds')
soup = BeautifulSoup(page.content, 'html5lib')

header = soup.find("span", {"id": "List_of_Backgrounds"}).parent
backgroundSection = header.findNext('ul')
for listItem in backgroundSection:
    link = listItem.find('a', href=True)['href']
    background = listItem.find('a', href=True).string
    # clean up the link a bit.
    # http://engl393-dnd5th.wikia.com/wiki/Initiate
    # we can ignore edit links
    if 'action=edit' not in link:
        if link.startswith('/'):
            backgroundUrl = baseURL + link

    # link is now clean and we can work with it.
    page = requests.get(backgroundUrl)
    soup = BeautifulSoup(page.content, 'html5lib')
    tables = soup.findAll('table')
    if tables:
        print(background + ' => ' + backgroundUrl)
        outputFile = 'data/' + background + '.csv'
        with open(outputFile, 'w', newline='') as csvfile:
            rowWriter = csv.writer(csvfile, delimiter='\t')
            # CSV.writerow takes an iterable, strings will be broken into a list, so cast it to a list first.
            for table in soup.findAll('table'):
                for row in table.findAll('tr'):
                    if row.findAll('th'):
                        row = [elem.text.strip() for elem in row.findAll('th')]
                        rowWriter.writerow(row)
                    else:
                        row = [elem.text.strip() for elem in row.findAll('td')]
                        rowWriter.writerow(row)
