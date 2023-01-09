from the_higher_lower_art import logo, vs
from the_higher_lower_data import data
from random import choice

print(logo)
a = choice(data)
print(f"{a['name']}, {a['description']}, {a['country']}")

print(vs)

b = choice(data)
print(f"{b['name']}, {b['description']}, {b['country']}")

