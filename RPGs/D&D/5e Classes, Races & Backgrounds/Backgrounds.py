from bs4 import BeautifulSoup
import csv
import requests

url = 'https://www.dndbeyond.com/backgrounds'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

allBackgrounds = []
fullBackgrounds = []
fullBackgroundLinks = []
fullBackgroundSources = ['Basic Rules', 'Curse of Strahd: Character Options']

for background in soup.findAll('div', {'class' : 'list-row-background'}):
	source = background.find('div', {'class' : 'list-row-name-secondary-text'}).text.strip()
	if source in fullBackgroundSources:
		link = background.find('div', {'class' : 'list-row-name-primary-text'}).find('a')['href']
		link = link.replace('/backgrounds', '')
		fullBackgroundLinks.append(link)

	allBackgrounds.append([
		background.find('div', {'class' : 'list-row-name-primary-text'}).text.strip(),
		background.find('div', {'class' : 'list-row-feature-primary-text'}).text.strip(),
		background.find('div', {'class' : 'list-row-proficiencies-primary-text'}).text.strip(),
		background.find('div', {'class' : 'list-row-tags-primary-text'}).text.strip(),
	])

file = open('backgrounds.csv', 'w')
with file:
	writer = csv.writer(file)
	writer.writerows(allBackgrounds)

# Full background time!
for link in fullBackgroundLinks:
	page = requests.get(url + link)
	soup = BeautifulSoup(page.content, 'lxml')

	title = soup.find('h1', {'class' : 'page-title'}).text.strip().replace('/', '-')

	file = open('data/' + title + '.html', 'w')
	file.write('<h1>' + title + '</h1>\n')
	file.write(str(soup.find('div', {'class' : 'details-container-content-description-text'})))
