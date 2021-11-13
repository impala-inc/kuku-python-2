# x_2_1
#
# パラメーター名を引数に取り、桃太郎のデータを返す「momotaro_data()」を定義してください。

momotaro = {
    '名前': '桃太郎',
    'ヒットポイント': 1800,
    '攻撃力': 230,
    '守備力': 200,
}


def momotaro_data(parameter):
    return momotaro[parameter]


data = momotaro_data('ヒットポイント')
print(data)


# こちらでも良い
#
# def momotaro_data(parameter):
#     momotaro = {
#         '名前': '桃太郎',
#         'ヒットポイント': 1800,
#         '攻撃力': 230,
#         '守備力': 200,
#     }
#     return momotaro[parameter]
