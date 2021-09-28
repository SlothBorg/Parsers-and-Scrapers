import csv

combinations = []
valid_combos = []
with open('combos', 'r') as f:
    combinations = list(csv.reader(f,delimiter='\t'))

for row in combinations:
    if 'Shape' not in row:
        valid_combos.append(row)
    else:
        index = row.index('Shape')
        if index > 0 and row[index-1] == 'Pull':
            valid_combos.append(row)
        elif index + 1 < len(row) and row[index+1] == 'Push':
            valid_combos.append(row)

for row in valid_combos:
    print('\t'.join(str(x) for x in row))