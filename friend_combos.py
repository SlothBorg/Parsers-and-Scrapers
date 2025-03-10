import itertools
import random

friends = [
    'Elias-Joh',
    'Amy',
    'Yeti',
    'Kristen',
    'Larissa',
    'Lukas',
    'Raven',
    'Topaz',
    'Sherdyl',
    'Nic',
    'Niki',
    'Olivia',
]

combos = list(itertools.permutations(friends, 2))

wedding = random.choice(combos)
print(f"lets celebrate the wedding of {wedding[0]} and {wedding[1]}")
