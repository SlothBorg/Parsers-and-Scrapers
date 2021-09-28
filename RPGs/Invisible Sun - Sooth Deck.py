from bs4 import BeautifulSoup
import csv
import requests

def get_card_part(card, search):
	i = 0
	for string in card.find_all('p'):
		if string.text.find(search) > -1:
			return string.text.replace(search, '')

def get_card_data(card):
	return [
		# Title
		card.find('h2').text.title(),
		# Flavor
		card.find('p', {'class' : 'flavor'}).text,
		# Secrets
		card.find('strong').text.replace('Secrets • ', '').replace(' •', ','),
		# Meanings
		get_card_part(card, 'Meanings: '),
		# Game Narrative
		get_card_part(card, 'Game Narrative: '),
		# Divination
		get_card_part(card, 'Divination: '),
		# Joy
		get_card_part(card, 'Joy: '),
		# Despair
		get_card_part(card, 'Despair: ')
	]
cards = []
cardNumber = ["%.2d" % i for i in range(1, 61)]
for number in cardNumber:
	print('Getting card ' + str(number))
	url = 'http://app.invisiblesunrpg.com/soothdeck/card-' + str(number)
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html5lib')

	title = soup.find('h2').text.title()
	cardName = str(number) + ' ' + title + '.html'
	card = soup.find('article', {'class': 'type-page'})

	cards.append(get_card_data(card))
	with open(cardName, 'w') as textFile:
		print('Writing: ' + cardName)
		content = str(card)
		textFile.write(content)

with open('Sooth Deck.csv', 'w', newline='') as csvfile:
	rowWriter = csv.writer(csvfile, delimiter='\t')
	headers = ['Title', 'Flavor', 'Secrets', 'Meanings', 'Game Narrative', 'Divination', 'Joy', 'Despair']
	rowWriter.writerow(headers)
	for card in cards:
		rowWriter.writerow(card)
