# x_6_8
#
#

class StockError(Exception):
    pass


order_count = input('きび団子を何個注文しますか？:')

try:
    try:
        if int(order_count) > 100:
            raise StockError
    except ValueError:
        print('数字を入力してください')
except StockError:
    print('在庫切れです')
else:
    print('ご購入ありがとうございます')
finally:
    print('ご利用ありがとうございました')
