from glob import glob
from csv import reader


def select_file():
    files = glob('Data/*.csv')
    display_files(files)
    file = get_file(files)
    return files[file]


def display_files(files):
    for index, file in enumerate(files):
        print(str(index) + '\t' + file)


def get_file(files):
    file = -1
    while file < 0 or file > len(files)-1 :
        try:
            file = int(input("Select a file to parse: "))
        except ValueError:
            print('You must enter a number')
    return file

def file_to_list(file):
    monsters = []
    with open(file) as csv_file:
        csv_reader = reader(csv_file)
        for line in csv_reader:
            if line:
                monsters.append(line)

    # return list(map(lambda x: x.pop(0), monsters))
    return monsters


def parse_monsters(monsters):
    clean_monsters = []
    headers = []
    for index, value in enumerate(monsters):
        if index == 0:
            # CSV header line
            headers = value
            print(value)
        # print(value[1])
        elif value[1] not in clean_monsters:
            clean_monsters.append(value)
    return clean_monsters


if __name__ == '__main__':
    file = select_file()
    print("Parsing " + str(file))
    monsters = file_to_list(file)
    clean_monsters = parse_monsters(monsters)
    print(list(map(lambda x: x.pop(1), clean_monsters)))
