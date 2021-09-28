from bs4 import BeautifulSoup
import csv
import requests

page = requests.get('https://www.dndbeyond.com/races')
soup = BeautifulSoup(page.content, 'lxml')

allRaces = []

# raceDivs = soup.findAll('div', {'class' : 'j-collapsible ddb-collapsible'})
# for div in raceDivs:
races = soup.findAll('li', {'class' : 'listing-card'})
for race in races:
	allRaces.append([
		race.find('h3', {'class' : 'listing-card__title'}).text.strip(),
		race.find('div', {'class' : 'listing-card__source'}).text.strip(),
		race.find('div', {'class' : 'listing-card__description'}).find('p').text.strip(),
		race.find('p', {'class' : 'characters-statblock'}).text.strip()
	])

file = open('races.csv', 'w')
with file:
    writer = csv.writer(file)
    writer.writerows(allRaces)