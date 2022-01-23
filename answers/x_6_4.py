# 6の段「エラーと例外処理 ~ 4」
#
# 数字以外の値を入力した場合は「ValueError。数字を入力してください」と表示されます
# 0を入力した時に「ZeroDivisionError。0以外の数字を入力してください」と表示するようにコードを追加してください

total_price = 4000
number_of_people = input('合計で4000円です。何人でお支払いされますか？:')

try:
    price = total_price // int(number_of_people)
    print('お一人あたり' + str(price) + '円のお支払いになります')
except ValueError:
    print('ValueError。数字を入力してください')
except ZeroDivisionError:
    print('ZeroDivisionError。0以外の数字を入力してください')
