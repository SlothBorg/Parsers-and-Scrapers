import json


TEST = [
  {
    "id": 1,
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "age": 29,
    "is_active": True,
    "roles": ["admin", "editor"]
  },
  {
    "id": 2,
    "name": "Bob Smith",
    "email": "bob@example.com",
    "age": 35,
    "is_active": False,
    "roles": ["viewer"]
  },
  {
    "id": 3,
    "name": "Charlie Davis",
    "email": "charlie@example.com",
    "age": 42,
    "is_active": True,
    "roles": ["editor"]
  },
  {
    "id": 4,
    "name": "Dana White",
    "email": "dana@example.com",
    "age": 27,
    "is_active": True,
    "roles": ["admin"]
  }
]

WALLS = {
    'curved wall' : 'H-TRP-Sewer-Wall-v3.5.stl',
    'concave corner' : 'I-1-TRP-Sewer-Wall-v3.5.stl',
    'convex corner' : 'I-2B-Sewers-v0.14.stl',
    'short wall' : 'll-TRP-Sewer-Wall-v3.5.stl',
    'wall' : 'S-1-TRP-Sewer-Wall-v3.5.stl',
    'concave corner wall' : 'S-2-TRP-Sewer-Wall-v3.5.stl',
    'convex corner wall - with pipe' : 'S-3-TRP-Sewer-Wall-v3.6.stl',
    'wall - grate' : 'S-TRP-Sewer-Grate-v3.5.stl',
    'wall - ladder' : 'S-TRP-Sewer-Ladder-v3.5.stl',
    'wall - valve' : 'S-TRP-Sewer-Valve-v3.5.stl'
}
FLOORS = {
    'AS-TRP-1-v1.0.stl' : 'thin lower + raised',
    'E-TRP-Sewer-1-v1.0.stl' : 'lower + raised',
    'E-TRP-Sewer-2-v1.0.stl' : 'lower + raised T junction',
    'E-TRP-Sewer-3-v2.0.stl' : 'lower + raised 4 way junction',
    'E-TRP-Sewer-4-v2.0.stl' : 'lower + raised - end with path',
    'E-TRP-Sewer-5-v2.0.stl' : 'lower + raised - corner raised edge',
    'E-TRP-Sewer-6-v2.0.stl' : 'lower + raised - circular end',
    'E-TRP-Sewer-7-v2.0.stl' : 'raised',
    'E-TRP-Sewer-8-v2.0.stl' : 'lower + raised - square end',
    'E-TRP-Sewer-9-v2.1.stl' : 'thin raised + lower',
    'E-TRP-Sewer-10-v2.1.stl' : 'lower + raised - corner',
    'E-TRP-Sewer-11-v1.0.stl' : 'lower',
    'F-TRP-Sewer-1-v2.0.stl' : 'curved lower + raised - corner raised edge',
    'F-TRP-Sewer-2-v1.0.stl' : 'curved lower + raised - corner',
}


if __name__ == '__main__':
    print(json.dumps(TEST))