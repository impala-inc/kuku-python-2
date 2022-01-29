# x_1_8
#
# 関数「drink()」が戻り値で飲み物の名前だけを返すように修正してください

age = int(input('年齢を入力してください:'))


def drink(age):
    if age <= 12:
        print('オレンジジュースをどうぞ')
        return

    if age >= 20:
        osake = input('お酒は好きですか？(はい/いいえ):')
        if osake == 'はい':
            print('ビールをどうぞ')
            return

    print('烏龍茶をどうぞ')


drink(age)
