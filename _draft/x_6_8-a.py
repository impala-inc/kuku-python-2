# x_6_8
#
#

class StockError(Exception):
    pass


class NumberError(Exception):
    pass


order_count = input('きび団子を何個注文しますか？:')
card_number = input('カード番号を入力してください？(例、0000-0000):')

try:
    if int(order_count) > 100:
        raise StockError
    if card_number != '1111-1111':
        raise NumberError
except StockError:
    print('在庫切れです')
except NumberError:
    print('カードエラー')
else:
    print('ご購入ありがとうございます')
finally:
    print('ご利用ありがとうございました')
