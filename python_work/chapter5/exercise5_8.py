users = ['admin','user1','user2','user3','user4']

for user in users:
    if user == 'admin':
        print(f"Hello {user},would you like to see a status report?")
    else:
        print(f"Hello {user},thank you for logging again.")

# exercise5_9
users = []

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user},would you like to see a status report?")
        else:
            print(f"Hello {user},thank you for logging again.")
else:
    print("We need to find some users!")
    