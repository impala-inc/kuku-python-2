# x_1_9
#
# 処理が共通している部分を関数にしてください

import random

momotaro = {
    '名前': '桃太郎',
    'ヒットポイント': 1800,
    '攻撃力': 230,
    '守備力': 200,
    '命中率': 80,
}

aka_oni = {
    '名前': '赤鬼',
    'ヒットポイント': 2500,
    '攻撃力': 250,
    '守備力': 250,
    '命中率': 50,
}


def attack(attacker, defender):
    point = (attacker['攻撃力'] - (defender['守備力'] / 2)) * \
        (random.randint(attacker['命中率'], 100) / 100)
    print(defender['名前'] + 'は' + str(point) + 'のダメージを受けた')


attack(momotaro, aka_oni)
attack(aka_oni, momotaro)
