import itertools

strings = ['Peer', 'Pull', 'Push', 'Seek', 'Shape']
tmp = []
combinations = []

for x in range(1, len(strings)+1):
    combinations.extend(list(itertools.permutations(strings, x)))

for row in combinations:
    print('\t'.join(str(x) for x in row))
