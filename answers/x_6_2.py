
# 6の段「エラーと例外処理 ~ 2」
#
# 「おわり4」まで表示できるようにコードを修正してください

try:
    raise IndexError
except IndexError:
    print('IndexErrorエラーを無視します')


print('おわり1')

try:
    raise TypeError
except TypeError:
    print('TypeErrorエラーを無視します')

print('おわり2')

try:
    raise ValueError
except ValueError:
    print('ValueErrorエラーを無視します')

print('おわり3')

try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print('ZeroDivisionErrorエラーを無視します')

print('おわり4')
