# x_1_6
#
# 実行する度に「グー、チョキ、パー」がランダムで返る「janken()」という関数を定義してください。

import random


def janken():
    hands = ['グー', 'チョキ', 'パー']
    return random.choice(hands)


result = janken()
print(result)
