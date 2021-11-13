# x_2_9
#
# 「2-8」のように関数の中で自分自身を呼び出すものを「再帰関数」といいます
# 再帰関数を使って全てのメンバーを１行づつ表示してください
# ヒント値がリストがどうかを「type(members) == list」で判定します

members = [
    ['桃太郎', 'いぬ', 'さる', 'きじ', ['赤鬼', '青鬼', '黄鬼']],
    ['かに', 'くり', 'うす', 'はち', '牛糞', ['さる']],
    ['浦島太郎', 'かめ', '乙姫', 'たい', 'ひらめ', ['つる']],
]


def loop(members):
    if type(members) == list:
        for member in members:
            loop(member)
    else:
        print(members)


loop(members)
