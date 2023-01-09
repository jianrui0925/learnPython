pizzas = ["火腿","菠萝","鸡肉","牛肉"]
for pizza in pizzas:
    print(f"我喜欢{pizza}披萨。")
print("我超级喜欢披萨！")
# exercise4_11
friend_pizzas = pizzas[:]
pizzas.append("蔬菜")
friend_pizzas.append("培根")
print(f"我喜欢的披萨是：")
for pizza in pizzas:
    print(pizza)
print(f"朋友喜欢的披萨是：")
for pizza in friend_pizzas:
    print(pizza)