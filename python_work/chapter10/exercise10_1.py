filename = 'learn_python.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

# with open(filename) as file_object: