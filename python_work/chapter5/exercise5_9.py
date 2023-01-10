current_users = ['admin','John','Lora','Jack','mike']
current_users_copy = []
for user in current_users:
    user_copy = user.lower()
    # print(user_copy)
    current_users_copy.append(user_copy)

new_users = ['john','coco']

for user in new_users:
    if user.lower() in current_users_copy:
        print('用户名已被使用！')
    else:
        print('可以使用的用户名！')