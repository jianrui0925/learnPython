import json

filename = 'favoriteNum.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    print(f"file not found.")
print(f"Your favorite number is {number}.")
