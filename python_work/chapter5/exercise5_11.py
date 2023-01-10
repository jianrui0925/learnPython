numbers = [number for number in range(1,10)]
# print(numbers)
for value in numbers:
    if value == 1:
        print("1st")
    elif value == 2:
        print("2nd")
    elif value == 3:
        print("3rd")
    else:
        print(f"{value}th")