import json
from itertools import combinations, product


WALLS_PS = [
    {
        "id": 1,
        "file_name": "H-TRP-Sewer-Wall-v3.5.stl",
        "type": "wall",
        "length": "normal",
        "orientation": "curved",
        "angle": "",
        "details": ""
    },
    {
        "id": 2,
        "file_name": "I-1-TRP-Sewer-Wall-v3.5.stl",
        "type": "corner",
        "length": "short",
        "orientation": "curved",
        "angle": "concave",
        "details": ""
    },
    {
        "id": 3,
        "file_name": "I-2B-Sewers-v0.14.stl",
        "type": "corner",
        "length": "short",
        "orientation": "curved",
        "angle": "convex",
        "details": ""
    },
    {
        "id": 4,
        "file_name": "ll-TRP-Sewer-Wall-v3.5.stl",
        "type": "wall",
        "length": "short",
        "orientation": "straight",
        "angle": "",
        "details": ""
    },
    {
        "id": 5,
        "file_name": "S-1-TRP-Sewer-Wall-v3.5.stl",
        "type": "wall",
        "length": "normal",
        "orientation": "straight",
        "angle": "",
        "details": ""
    },
    {
        "id": 6,
        "file_name": "S-2-TRP-Sewer-Wall-v3.5.stl",
        "type": "corner wall",
        "length": "normal",
        "orientation": "straight",
        "angle": "concave",
        "details": ""
    },
    {
        "id": 6,
        "file_name": "S-3-TRP-Sewer-Wall-v3.6.stl",
        "type": "corner wall",
        "length": "normal",
        "orientation": "straight",
        "angle": "convex",
        "details": "pipe"
    },
    {
        "id": 7,
        "file_name": "S-TRP-Sewer-Grate-v3.5.stl",
        "type": "wall",
        "length": "normal",
        "orientation": "straight",
        "angle": "",
        "details": "grate"
    },
    {
        "id": 8,
        "file_name": "S-TRP-Sewer-Ladder-v3.5.stl",
        "type": "wall",
        "length": "normal",
        "orientation": "straight",
        "angle": "",
        "details": "ladder"
    },
    {
        "id": 9,
        "file_name": "S-TRP-Sewer-Valve-v3.5.stl",
        "type": "wall",
        "length": "normal",
        "orientation": "straight",
        "angle": "",
        "details": "valve"
    }
]

FLOORS_PS = [
    {
        "id": 1,
        "file_name": "E-TRP-Sewer-1-v1.0.stl",
        "type": "floor",
        "length": "normal",
        "orientation": "straight",
        "angle": "",
        "details": ""
    },
    # 'E-TRP-Sewer-1-v1.0.stl' : 'lower + raised',
    # 'E-TRP-Sewer-2-v1.0.stl' : 'lower + raised T junction',
    # 'E-TRP-Sewer-3-v2.0.stl' : 'lower + raised 4 way junction',
    # 'E-TRP-Sewer-4-v2.0.stl' : 'lower + raised - end with path',
    # 'E-TRP-Sewer-5-v2.0.stl' : 'lower + raised - corner raised edge',
    # 'E-TRP-Sewer-6-v2.0.stl' : 'lower + raised - circular end',
    # 'E-TRP-Sewer-7-v2.0.stl' : 'raised',
    # 'E-TRP-Sewer-8-v2.0.stl' : 'lower + raised - square end',
    # 'E-TRP-Sewer-9-v2.1.stl' : 'thin raised + lower',
    # 'E-TRP-Sewer-10-v2.1.stl' : 'lower + raised - corner',
    # 'E-TRP-Sewer-11-v1.0.stl' : 'lower',
    # 'F-TRP-Sewer-1-v2.0.stl' : 'curved lower + raised - corner raised edge',
    # 'F-TRP-Sewer-2-v1.0.stl' : 'curved lower + raised - corner',
]

WALLS_ULVHEIM = [
    'corner_inner.stl',
    'corner_outer.stl',
    'wall_opening.stl',
    'wall_straight.stl'
]

FLOORS_ULVHEIM = [
    'floor_corner.stl',
    'floor_straight.stl',
    # 'floor_x.stl',
    'floor_main.stl'
]


if __name__ == '__main__':
    wall_combos = list(product(WALLS_ULVHEIM, repeat=2))

    result = [(a, b, c) for (a, b) in wall_combos for c in FLOORS_ULVHEIM]

    all_results = result + [('floor_tee.stl', b, c) for (b, c) in wall_combos for c in FLOORS_ULVHEIM]

    for combo in all_results:
        if len(combo) == 3:
            print(f"{combo[0]} + {combo[2]} + {combo[1]}")
        else:
            print(f"{combo[0]} + {combo[1]}")