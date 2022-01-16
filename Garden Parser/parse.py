from bs4 import BeautifulSoup
import csv


def load_content(file):
    with open(file, 'r') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
        return soup.find('div', {'class': 'companion-plant-index'})


def chunck_content(content):
    data = []
    for section in content.prettify().split('<hr/>\n'):
        data.append(section)
    return data


def parse_content(sections):
    data = []
    for section in sections:
        section_data = []
        soup = BeautifulSoup(section, 'lxml')
        section_data.append(soup.find('h3').text.strip())
        good_companions = soup.find('div', {'class': 'good-companions'}).find("ul")
        section_data.append(get_list_elements(good_companions))
        bad_companions = soup.find('div', {'class': 'bad-companions'}).find("ul")
        section_data.append(get_list_elements(bad_companions))
        name = soup.find('p')
        if not isinstance(name, type(None)):
            section_data.append(name.text.replace(',', '').strip())

        data.append(section_data)
    return data


def get_list_elements(list):
    data = ''
    for li in list.find_all("li"):
        data += li.text.strip() + ' '
    return data.rstrip()


def write_content(list, file):
    with open(file, 'w', newline='') as csvfile:
            file_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            headings = ['Plant', 'Good Companions', 'Bad Companions', 'Notes']
            file_writer.writerow(headings)
            for item in list:
                file_writer.writerow(item)

if __name__ == '__main__':
    in_file = 'list_1.html'
    out_file = 'output.csv'

    content = load_content(in_file)
    chuncks = chunck_content(content)
    lists = parse_content(chuncks)
    write_content(lists, out_file)
