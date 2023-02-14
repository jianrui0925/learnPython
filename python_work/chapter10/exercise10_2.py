with open('learn_python.txt') as file_object:
    lines = file_object.readlines()
str_a = ""
for line in lines:
    print(line.strip())
    str_a += line.strip()
str_a.replace('python','c')
print(str_a)
