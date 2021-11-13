# x_1_6
#
# 実行する度に「グー、チョキ、パー」がランダムで返る「janken()」という関数を定義してください。

import random

hands = ['グー', 'チョキ', 'パー']
result = random.choice(hands)

print(result)
