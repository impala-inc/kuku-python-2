# 6の段「エラーと例外処理 ~ 1」
#
# 「おわり4」まで表示できるようにコードを修正してください

try:
    ['桃太郎', 'いぬ', 'さる', 'とり'][5]  # IndexErrorエラーが発生
except IndexError:
    print('IndexErrorエラーを無視します')


print('おわり1')

100 + 'あいうえお'

print('おわり2')

int('あいうえお')

print('おわり3')

100 / 0

print('おわり4')
