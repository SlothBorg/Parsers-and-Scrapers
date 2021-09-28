from bs4 import BeautifulSoup
import csv
from datetime import datetime
import glob

titles = []

with open('courses.csv', 'w', newline='') as output:
    writer = csv.writer(output, delimiter=' ')

    for file in glob.glob("*.html"):
        print('Parsing: ' + file)

        soup = BeautifulSoup(open(file, 'r', encoding="utf-8"), 'lxml')
        container = soup.find('ul', {'class' : 'shopping-list'})

        for li in container.findAll('li', {'class' : 'clearfix'}):
            date = li.find('div', {'class' : 'history-detail__created'})
            if date is not None:
                # normalize months:
                date_str = date.contents[0].upper().replace('SEPT', 'SEP').replace('JULY', 'JUL').replace('JUNE', 'JUN').replace('APRIL', 'APR').replace('.', '')
                date_str = datetime.strptime(date_str, '%b %d, %Y')

                title_label = li.find('label', {'class' : 'shopping-list__course-title'})

                for link in li.findAll('a', {'class' : 'shopping-list__course-title'}):
                    print([date_str.strftime('%Y/%m/%d'), link.contents[0], link['href']])
                    writer.writerow([date_str.strftime('%Y/%m/%d'), link.contents[0], link['href']])
