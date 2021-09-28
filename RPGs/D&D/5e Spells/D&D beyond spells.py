from bs4 import BeautifulSoup
import requests
import re
import csv

def getPage(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib')
    return soup

def getSpellDetails(spellData):
    info = {}
    valueClass = {'class' : 'ddb-statblock-item-value'}
    detailClass = 'ddb-statblock-item-'
    details = ['level', 'casting-time', 'range-area', 'components', 'duration', 'school', 'attack-save', 'damage-effect']

    for spellDetail in details:
        data = spellData.find('div', {'class' : detailClass + spellDetail})
        if None != data:
            dataValue = data.find('div', valueClass)
            info[spellDetail] = ' '.join(dataValue.text.split())

    return info

def getSpellDescription(spellData):
    info = {}
    description = spellData.find('div', {'class' : 'more-info-content'})
    if None != description:
        # if there is a clarification on what the component is
        component = description.find('span', {'class' : 'components-blurb'})
        if None != component:
            info['Component Detail'] = component.text.strip()
        # handel the description text
        descriptionText = []
        for d in description.findAll('p'):
            descriptionText.append(str(d.text))
        info['Description'] = '\n'.join(descriptionText)

    return info


contentDiv = 'info'
rawSpellList = []
spellBook = []
outputFile = 'Spells.csv'
baseURL = 'https://www.dndbeyond.com/spells'
querry = ''
lastPage = False
while not lastPage:
    # We don't yet know if it's the last page, so assume it is.
    lastPage = True
    soup = getPage(baseURL + querry)
    content = soup.findAll('div', {'class' : 'info'})
    for spell in content:
        rawSpellList.append(spell)

    nextButtons = soup.findAll('li', {'class' : 'b-pagination-item'})
    for button in nextButtons:
        if button.text == 'Next':
            querry = button.a.get('href').replace('/spells', '')
            lastPage = False
            break
headings = []

for spell in rawSpellList:
    spellInfo = {}
    # get name
    name = spell.find('a', {'class' : 'link'})
    spellInfo['Name'] = name.text
    spellInfo['URL'] = baseURL + name['href'].replace('/spells', '')

    spellData = getPage(spellInfo['URL'])

    # Get info from the detail page
    spellDetails = getSpellDetails(spellData)
    if spellDetails:
        spellInfo.update(spellDetails)

    spellDescription = getSpellDescription(spellData)
    if spellDescription:
        spellInfo.update(spellDescription)

    if not headings:
        headings = spellInfo.keys()
        print(headings)

    spellBook.append(spellInfo)

with open(outputFile, 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    csvRow = csv.writer(csvfile, delimiter='\t')
    csvRow.writerow(headings)
    for spell in spellBook:
        # for key, value in spell.items():
        #     print([value])
        # write the info to a CSV
        csvRow.writerow([v for k, v in spell.items()])
