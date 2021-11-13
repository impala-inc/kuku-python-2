# x_1_5
#
# 「1-2」では関数を実行した結果を「name」と「favorite」という変数に代入しました。
# 関数を実行した際に関数から返って来る値を「戻り値（返り値）」と言い、「return」の後ろに返したい値を置きます。
# 「1-4」の計算結果を関数内で「print()」で表示するのではなく、戻り値で返して実行結果を表示するように修正してください。

def tasu(a, b):
    return a + b


result = tasu(123, 254)
print(result)


def hiku(a, b):
    return a - b


result = hiku(123, 254)
print(result)


def kakeru(a, b):
    return a * b


result = kakeru(123, 254)
print(result)


def waru(a, b):
    return a / b


result = waru(123, 254)
print(result)
