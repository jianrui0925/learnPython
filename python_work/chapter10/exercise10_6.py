print(f"Please input two numbers.")
num1 = input()
num2 = input()
try:
    sum = int(num1) + int(num2)
except:
    print(f"You must input two numbers.")
else:
    print(f"Two numbers sum:{sum}")
