import requests
import re
import csv

# def get_number(prompt):
#   while True:
#     try:
#        userInput = int(input(prompt))
#     except ValueError:
#        print("Not an integer! Try again.")
#        continue
#     else:
#        return userInput

# sides = get_number("# of sides: ")
# number = get_number("Pool size: ")
# target_high = get_number("Highest TN #: ")
# target_low = get_number("Lowest TN #: ")
# target_numbers = [i for i in range(target_low, (target_high+1))]
# base_regex = '.*?([+-]?\d*\.\d+)(?![-+0-9\.])'

base_regex = '[\+-]?[0-9]*[\.]?[0-9]+([eE][\+-]?[0-9]+)?'
sides = 8
target = 4
for number in range(1, 11):
    url = 'http://www.unseelie.org/cgi-bin/dicepo.cgi?number='
    url += str(number) + '&sides=' + str(sides) + '&target=' + str(target)
    url += '&cumulus=1&action=Press+once+to+send'
    # print(url)
    page = requests.get(url)
    page = page.content.decode("utf-8")

    results = []
    for i in range(0, (number+1)):
        if 0 == i:
            regex = '(no successes is )' + base_regex
        elif 1 == i:
            regex = '(1 success or more is )' + base_regex
        else:
            regex = '( ' + str(i) + ' successes or more is )' + base_regex
        results.append(re.search(regex, page).group(0).strip())

    output = []
    for result in results:
        # print(result)
        # print(result.split('is ')[1])
        output.append(result.split('is ')[1])
    print(output)

    output_file = open('outpute.csv', 'a', newline='')
    writer = csv.writer(output_file, delimiter=',')
    writer.writerow(output)
