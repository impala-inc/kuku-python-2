# 6の段「エラーと例外処理 ~ 1」
#
# 数字以外の値を入力した場合は

try:
    1000 + 'あああああ'
except TypeError:
    print('TypeErrorが発生したようですが続行します')


total_price = 4000
number_of_people = input('合計で4000円です。何人でお支払いされますか？:')

price = total_price // int(number_of_people)
print('お一人あたり' + str(price) + '円のお支払いになります')
