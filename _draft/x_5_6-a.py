# x_5_6
#
#


import random


class Oni:
    def __init__(self, number):
        self.name = f"{number}ノ鬼"
        self.hp = random.randint(170, 255)
        self.power = random.randint(170, 255)


numbers = ['壱', '弐', '参', '肆', '伍', '陸', '漆', '捌', '玖', '拾']
onis = []
i = 0

while i < 10:
    onis.append(Oni(numbers[i]))
    i += 1

for oni in onis:
    print(f'{oni.name} HP: {oni.hp} 力: {oni.power}')
