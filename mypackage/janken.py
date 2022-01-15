import random

HANDS = ['グー', 'チョキ', 'パー']


class Janken():
    def __init__(self):
        self.hand = random.choice(HANDS)

    def __eq__(self, other):  # 「__eq__()」を定義するとselfとotherを「==」で比較できる
        return self.hand == other.hand

    def __gt__(self, other):  # 「__gt__()」を定義するとselfとotherを「>」で比較できる
        diff = HANDS.index(self.hand) - HANDS.index(other.hand)
        return diff == -1 or diff == 2
