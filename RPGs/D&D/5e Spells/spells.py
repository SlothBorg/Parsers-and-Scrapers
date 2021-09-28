import bs4
from bs4 import BeautifulSoup
import csv
import requests

contentDiv = 'mw-content-text'
baseURL = 'http://engl393-dnd5th.wikia.com'

def getSpellDescrtiption(url):
    page = requests.get(baseURL + url)
    soup = BeautifulSoup(page.content, 'html5lib')
    content = soup.find('div', {'class': contentDiv})
    spellDescription = ''
    for line in content.findAll('p'):
        spellDescription += str(line)
    return spellDescription

spellList = {}
outputFile = 'Spells.csv'
page = requests.get(baseURL + '/wiki/Wizard_Spells')
spellClasses = [
    'Wizard_Spells',
    'Warlock_Spells',
    'Sorcerer_Spells',
    'Paladin_Spells',
    'Druid_Spells',
    'Cleric_Spells',
    'Bard_Spells',
    'Ranger_Spells'
]

soup = BeautifulSoup(page.content, 'html5lib')

content = soup.find('div', {'class': contentDiv})
lists = content.findAll('ul')

with open(outputFile, 'w', newline='') as csvfile:
    rowWriter = csv.writer(csvfile, delimiter='\t')
    for unorderedList in lists:
        for listItem in unorderedList:
            name = listItem.text.split('[')[0]
            if name not in spellList:
                url = listItem.find('a')['href']
                rowWriter.writerow([name, url, getSpellDescrtiption(url)])
                getSpellDescrtiption(url)
#                 spellList[name] = url

# for spell, url in spellList.items():
#     print(spell + ' ' + url)

