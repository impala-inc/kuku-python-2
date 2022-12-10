# x_5_9
#
#

import random


class Janken():
    def __init__(self):
        self.hand = random.choice(['グー', 'チョキ', 'パー'])

    def __eq__(self, other):
        return self.hand == other.hand

    def __gt__(self, other):
        return (self.hand == 'グー' and other.hand == 'チョキ') \
            or (self.hand == 'チョキ' and other.hand == 'パー') \
            or (self.hand == 'パー' and other.hand == 'グー')


a = Janken()
b = Janken()

print('aは' + a.hand)
print('bは' + b.hand)

if a == b:
    print('あいこ')
elif a > b:
    print('aの勝ち')
else:
    print('aの負け')
