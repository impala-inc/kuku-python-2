# 6の段「エラーと例外処理 ~ 1」
#
# 「おわり4」まで表示できるようにコードを修正してください

try:
    raise IndexError
except IndexError:
    print('IndexErrorエラーを無視します')


print('おわり1')

raise ValueError

print('おわり2')

raise TypeError

print('おわり3')

raise ZeroDivisionError

print('おわり4')
