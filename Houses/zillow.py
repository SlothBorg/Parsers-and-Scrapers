from bs4 import BeautifulSoup
import glob, os

def get_files():
	return glob.glob("*.html");

def list_files(files):
	i = 1
	for file in files:
		print(str(i) + "\t" + str(file))
		i+=1

def select_file(files):
	file = None
	while True:
		n = input('Which file would you like to parse? ')
		if validate_input(n, len(files)):
			break
		else:
			continue
	return files[int(n)-1]

def validate_input(number, length):
	return (int(number) and int(number) > 0 and int(number) <= length)

def load_file(file):
	print("Loading... " + file)
	with open(file, "r") as f:
		contents = f.read()
		return BeautifulSoup(contents, 'lxml')

def parse_file(soup):
	identifiers = {
		'address' : [
			'h1',
			'ds-address-container'
		],
		'price' : [
			'h3',
			'ds-price'
		],
		'price-change' : [
			'span',
			'ds-price-change'
		],
		'bed-bath-footage' : [
			'h3',
			'ds-bed-bath-living-area-container'
		],
		'mortgage' : [
			'div',
			'ds-mortgage-row'
		],
		'overview' : [
			'div',
			'ds-overview-section'
		],
	}
	data = {}
	for k, v in identifiers.items():
		print(k, v[0], v[1])
		# print(get_value_by_identifier(soup, k, v))
		# data[k] = get_value_by_identifier(soup, v)

	# print(data)

def get_value_by_identifier(soup, element, identifier):
	return soup.find("h1", {"class" : identifier})

# -----------------------------------------------------
if __name__ == "__main__":
	files = get_files()
	list_files(files)
	file = select_file(files)
	soup = load_file(file)
	parse_file(soup)
