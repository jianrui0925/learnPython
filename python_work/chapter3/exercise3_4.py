names = ["李瑞云","戴景正","高泽凡","张宇"]
print(f"{names[0]}，我想邀请你一起吃晚饭。")
print(f"{names[1]}，我想邀请你一起吃晚饭。")
print(f"{names[2]}，我想邀请你一起吃晚饭。")
print(f"{names[3]}，我想邀请你一起吃晚饭。")
# exercise3_5
print("戴景正无法赴约。")
names.remove("戴景正")
names.insert(1,"蹇锐")
print(f"{names[0]}，我想邀请你一起吃晚饭。")
print(f"{names[1]}，我想邀请你一起吃晚饭。")
print(f"{names[2]}，我想邀请你一起吃晚饭。")
print(f"{names[3]}，我想邀请你一起吃晚饭。")
# exercise3_6
print("我找到一个更大的餐桌！")
names.insert(0,"新嘉宾1")
names.insert(-1,"新嘉宾2")
names.append("新嘉宾3")
print(f"{names[0]}，我想邀请你一起吃晚饭。")
print(f"{names[1]}，我想邀请你一起吃晚饭。")
print(f"{names[2]}，我想邀请你一起吃晚饭。")
print(f"{names[3]}，我想邀请你一起吃晚饭。")
print(f"{names[4]}，我想邀请你一起吃晚饭。")
print(f"{names[5]}，我想邀请你一起吃晚饭。")
print(f"{names[6]}，我想邀请你一起吃晚饭。")

print(f"我一共邀请了{len(names)}人参加。")
# exercise3_7
print("我只能邀请两人吃饭。")
name = names.pop()
print(f"{name}，对不起！不能邀请你了。")
name = names.pop()
print(f"{name}，对不起！不能邀请你了。")
name = names.pop()
print(f"{name}，对不起！不能邀请你了。")
name = names.pop();
print(f"{name}，对不起！不能邀请你了。")
name = names.pop()
print(f"{name}，对不起！不能邀请你了。")
print(f"{names[0]},你还在邀请之列。")
print(f"{names[1]},你还在邀请之列。")
del names[0]
del names[0]
print(names)
# exercise3_9
print(f"我一共邀请了{len(names)}人参加。")