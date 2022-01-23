# 6の段「エラーと例外処理 ~ 1」
#
# エラーが起こった場合に「リストの範囲外です」と表示させてください

total_price = 4000
number_of_people = input('合計で4000円です。何人でお支払いされますか？:')

try:
    price = total_price // int(number_of_people)
    print('お一人あたり' + str(price) + '円のお支払いになります')
except:
    print('入力値が不正です')
