name = input("Please input your name.\r\n")
filename = "guest.txt"
with open(filename,'w') as f:
    f.write(name)