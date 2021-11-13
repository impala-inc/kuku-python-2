# x_2_2
#
# 6の目が二回連続して出るまで「saikoro()」を繰り返し実行してください

import random


def saikoro():
    result = random.randint(1, 6)
    print(str(result) + 'の目が出ました')
    return result


last_result = 0

saikoro()

while True:
    result = saikoro()

    if result == 6 and last_result == 6:
        break
    last_result = result
