from bs4 import BeautifulSoup
import csv
import requests

page = requests.get('https://www.dndbeyond.com/classes')
soup = BeautifulSoup(page.content, 'lxml')

allClasses = []

classes = soup.findAll('li', {'class' : 'listing-card'})
for pc in classes:
	allClasses.append([
		pc.find('img', {'class' : 'listing-card__icon'})["src"],
		pc.find('h3', {'class' : 'listing-card__title'}).text.strip(),
		pc.find('div', {'class' : 'listing-card__source'}).text.strip(),
		pc.find('div', {'class' : 'listing-card__description'}).find('p').text.strip(),
		pc.find('p', {'class' : 'characters-statblock'}).text.strip()
	])

file = open('classes.csv', 'w')
with file:
    writer = csv.writer(file)
    writer.writerows(allClasses)