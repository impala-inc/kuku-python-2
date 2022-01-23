# 6の段「エラーと例外処理 ~ 1」
#
# 「おわり２」が表示できるようにコードを修正してください

try:
    raise IndexError
except IndexError:
    print('エラーを無視します')


print('おわり１')

raise ValueError

print('おわり２')
