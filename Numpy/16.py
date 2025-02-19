import numpy as np

## Structured Arrays (Heterogeneous Data) ##
dtype = [('name', 'U10'), ('age', 'i4'), ('height', 'f4')]      # similar to a table in a database.

"""
name → Unicode string (max length 10)
age → Integer (4-byte)
height → Floating-point (4-byte)
"""

# Structured array
people = np.array(
    [('Alice', 25, 1.65), ('Bob', 30, 1.80), ('Charlie', 35, 1.75)],
    dtype=dtype
)

# print(people)

# print(people['name'])
# print(people['age'])

people['age'] = [26, 32, 38]
# print(people['age'])

tall_people = people[people['height'] > 1.75]
# print(tall_people['name'])


mytype = [('species', 'U20'), ('year', 'i4'), ('lived', 'i4')]

animals = np.array(
    [('Panthora', 2025, 110), ('Sapiens', 2025, 85), ('idk', 2000, 1000) ],
    dtype=mytype
)

# print(animals)