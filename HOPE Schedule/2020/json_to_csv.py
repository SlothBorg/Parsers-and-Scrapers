import json
import csv

with open('schedule.json') as json_file:
    schedule = json.load(json_file)

days = schedule['schedule']['conference']['days']

file_name = 'HOPE 2020 schedule.csv'
with open(file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, dialect=csv.excel, delimiter='\t')
    headers = ['Day', 'Title', 'Start', 'Length', 'Type', 'URL']
    csv_writer.writerow(headers)

    for day in days:
        for room in day['rooms']:
            for item in day['rooms'][room]:
                csv_writer.writerow([
                    day['index'],
                    item['title'].strip(),
                    item['start'].strip(),
                    item['duration'].strip(),
                    item['type'].strip(),
                    item['url'].strip(),
                ])
