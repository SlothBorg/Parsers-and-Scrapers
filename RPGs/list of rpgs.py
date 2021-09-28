from bs4 import BeautifulSoup
import csv
import requests


def parse_column(column):
    columnType = column.get('class')
    if columnType[0] == 'collection_rank':
        return column.text.strip()
    elif columnType[0] == 'collection_objectname':
        links = column.findAll('a')
        if len(links) == 1:
            return [links[0].text.strip(), '']
        elif len(links) > 1:
            data = links[0].text.strip()
            del links[0]
            return [data, ', '.join([x.text.strip() for x in links]) ]
    elif columnType[0] == 'collection_bggrating':
        return column.text.strip()
    else:
        return ''

# last page
baseURL = 'https://rpggeek.com/browse/rpg/page/'
page = requests.get(baseURL)
soup = BeautifulSoup(page.content, 'html5lib')
lastPage = int(soup.find('a', {'title' : 'last page'}).text.replace('[', '').replace(']', ''))

rpgs = []
for row in soup.findAll('tr', {'id' : 'row_'}):
    rpg = []
    for column in row.findAll('td'):
        data = parse_column(column)
        if isinstance(data, list):
            for item in data:
                rpg.append(item)
        else:
            rpg.append(data)
    rpgs.append(rpg)

for i in range(2, lastPage+1):
    page = requests.get(baseURL + str(i))
    print('Getting page ' + str(i) + '...')
    soup = BeautifulSoup(page.content, 'html5lib')

    for row in soup.findAll('tr', {'id' : 'row_'}):
        rpg = []
        for column in row.findAll('td'):
            data = parse_column(column)
            if isinstance(data, list):
                for item in data:
                    rpg.append(item)
            else:
                rpg.append(data)
        rpgs.append(rpg)

outputFile = 'RPGs.csv'
with open(outputFile, 'w', newline='') as csvfile:
    rowWriter = csv.writer(csvfile, delimiter='\t')
    # CSV.writerow takes an iterable, strings will be broken into a list, so cast it to a list first.
    headers = ['RPG Rank', 'Name', 'Family', 'Geek Rating', 'Avg Rating', 'Num Voters']
    rowWriter.writerow(headers)
    for rpg in rpgs:
        rowWriter.writerow(rpg)



# rpgs.append()


# for i in range(1, lastPage+1):


# header = soup.find("span", {"id": "List_of_Backgrounds"}).parent
# backgroundSection = header.findNext('ul')
# for listItem in backgroundSection:
#     link = listItem.find('a', href=True)['href']
#     background = listItem.find('a', href=True).string
#     # clean up the link a bit.
#     # http://engl393-dnd5th.wikia.com/wiki/Initiate
#     # we can ignore edit links
#     if 'action=edit' not in link:
#         if link.startswith('/'):
#             backgroundUrl = baseURL + link

#     # link is now clean and we can work with it.
#     page = requests.get(backgroundUrl)
#     soup = BeautifulSoup(page.content, 'html5lib')
#     tables = soup.findAll('table')
#     if tables:
#         print(background + ' => ' + backgroundUrl)
#         outputFile = 'data/' + background + '.csv'
#         with open(outputFile, 'w', newline='') as csvfile:
#             rowWriter = csv.writer(csvfile, delimiter='\t')
#             # CSV.writerow takes an iterable, strings will be broken into a list, so cast it to a list first.
#             for table in soup.findAll('table'):
#                 for row in table.findAll('tr'):
#                     if row.findAll('th'):
#                         row = [elem.text.strip() for elem in row.findAll('th')]
#                         rowWriter.writerow(row)
#                     else:
#                         row = [elem.text.strip() for elem in row.findAll('td')]
#                         rowWriter.writerow(row)
