people = [
    {"name": "harry", "house": "gryffindor"},
    {"name": "ron", "house": "ravenclaw"},
    {"name": "draco", "house": "slytherin"}
]


people.sort(key=lambda person: person["house"])

print(people)