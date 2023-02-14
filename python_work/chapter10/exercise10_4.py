while True:
    name = input("Please input your name,input q exit.\r\n")
    if(name == "q"):
        break;
    else:
        print(f"Hello {name}!")
        with open("guest.txt","a") as f:
            f.write(f"\r\n{name} arrive.")