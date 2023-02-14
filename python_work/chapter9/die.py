from random import randint
"""一个包含面数的色子类"""
class Die:
    def __init__(self,sides = 6):
        self.sides = sides
    def roll_die(self):
        print(randint(1,self.sides))
# a = Die()
# for i in range(1,6):
#     a.roll_die()