# x_5_6
#
#


import random


class Oni:
    def __init__(self, number):
        self.name = f"鬼{number}"
        self.hp = random.randint(170, 255)
        self.power = random.randint(170, 255)


oni_membesrs = []
i = 1

while i < 10:
    oni_membesrs.append(Oni(i))
    i += 1

for oni in oni_membesrs:
    print(f'{oni.name} HP: {oni.hp} 力: {oni.power}')
