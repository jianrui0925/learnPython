import json

number = input("What is your favorite number?")
filename = 'favoriteNum.json'
try:
    with open(filename,'w') as f:
        json.dump(number,f)
except FileNotFoundError:
    print(f"File save fail.")