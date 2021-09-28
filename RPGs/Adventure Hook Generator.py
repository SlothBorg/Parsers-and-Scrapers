import csv
import requests
import json

baseURL = 'https://www.rpgtablefinder.com/genie.php'
outputFile = 'Adventure Hooks.csv'

def appendIfNotInList(element, appendList):
    if element not in appendList:
        appendList.append(element)
listOfHooks = []
for i in range(0,7):
    listOfHooks.append([])

with open(outputFile, 'w', newline='') as csvfile:
    for x in range(0, 500):
        rowWriter = csv.writer(csvfile, delimiter='\t')
        page = requests.get(baseURL)
        hook = json.loads(page.content.decode("utf-8"))
        print(hook)
        rowWriter.writerow(hook)