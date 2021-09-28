import csv
import glob

# def getTitle():
# def getRange():
# def getSchool():
# def getComponents():

outputFile = 'AllSpells.csv'

with open(outputFile, 'w', newline='') as csvfile:
    for file in glob.glob('*.md'):
        with open(file) as f:
            content = f.readlines()
            content = filter(None, [x.strip() for x in content])

            for line in content:
                print('|' + str(line) + '|')
            # you may also want to remove whitespace characters like `\n` at the end of each line
            # print(file.replace('_', ' ').title())
            # print(content)
            # content[0] = name
            # content[1] = level
            # content[2] = school
            # rowWriter.writerow()