# 6の段「エラーと例外処理 ~ 1」
#
# 「おわり4」まで表示できるようにコードを修正してください

try:
    ['桃太郎', 'いぬ', 'さる', 'とり'][5]  # IndexErrorエラーが発生
except IndexError:
    print('IndexErrorエラーを無視します')

print('おわり1')

try:
    100 + 'あいうえお'
except TypeError:
    print('TypeErrorエラーを無視します')


print('おわり2')

try:
    int('あいうえお')
except ValueError:
    print('ValueErrorエラーを無視します')

print('おわり3')

try:
    100 / 0
except ZeroDivisionError:
    print('ZeroDivisionErrorエラーを無視します')

print('おわり4')
