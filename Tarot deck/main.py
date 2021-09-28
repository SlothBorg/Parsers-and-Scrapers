from bs4 import BeautifulSoup
import csv

def extract_grids():
    with open('html.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
        return soup.findAll('div', {'class': 'grid__item'})


def build_deck(grids):
    deck = []
    for grid in grids:
        suit_name = grid.get('id')
        if suit_name is not None:
            suit_name = suit_name.capitalize()
            if suit_name == 'Majorarcana':
                suit_name = 'Major Arcana'

            suit_meaning = grid.find('article', {'class': 'grid__item'}).getText().strip()
            if suit_meaning is not None:
                deck.append([suit_meaning, get_cards_from_grid(grid, suit_name)])
    return deck


def get_cards_from_grid(grid, suit_name):
    suit = []
    cards = grid.findAll('div', {'class': 'grid__item large--one-quarter medium--one-third text-center card'})
    for card in cards:
        card_name = card.find('h3').getText().strip(' Meaning')
        card_meanings = card.find('div', {'class': 'rte rte--indented-images'}).getText().strip()
        suit.append([suit_name, card_name, card_meanings])
    return suit


def write_cards_to_csv(deck):
    with open('Tarot Deck.csv', 'w', newline='') as csvfile:
        file_writer = csv.writer(csvfile, delimiter='\t', Jquoting=csv.QUOTE_MINIMAL)
        headings = ['Suit', 'Card', 'Meaning']
        file_writer.writerow(headings)
        for suit in deck:
            for cards in suit:
                if type(cards) == list:
                    for card in cards:
                            file_writer.writerow(card)
                else:
                    file_writer.writerow([cards])


if __name__ == '__main__':
    grids = extract_grids()
    deck = build_deck(grids)
    write_cards_to_csv(deck)
