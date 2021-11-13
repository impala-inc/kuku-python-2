# x_1_9
#
# 共通している処理を関数にしてください

import random

momotaro = {
    '名前': '桃太郎',
    'ヒットポイント': 1800,
    '攻撃力': 230,
    '守備力': 200,
}

aka_oni = {
    '名前': '赤鬼',
    'ヒットポイント': 2500,
    '攻撃力': 250,
    '守備力': 250,
}

momotaro_attack = ((momotaro['攻撃力'] / 2) - (aka_oni['守備力'] / 4)) * \
    (random.randint(7, 9) / 8)
print(aka_oni['名前'] + 'は' + str(momotaro_attack) + 'のダメージを受けた')

aka_oni_attack = ((aka_oni['攻撃力'] / 2) - (momotaro['守備力'] / 4)) * \
    (random.randint(7, 9) / 8)
print(momotaro['名前'] + 'は' + str(aka_oni_attack) + 'のダメージを受けた')
