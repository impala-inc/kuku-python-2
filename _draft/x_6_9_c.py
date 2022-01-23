# x_6_9
#
#

class CardErorr(Exception):
    pass


class StoreErorr(Exception):
    pass


class StockError(StoreErorr):
    pass


class ZipcodeError(StoreErorr):
    pass


class ExpiredError(CardErorr):
    pass


class NumberError(CardErorr):
    pass


order_count = input('きび団子を何個注文しますか？:')
zipcode = input('郵便番号を入力してください:')
card_number = input('カード番号を入力してください？(例、0000-0000-0000-0000):')
expired_at = input('有効期限を入力してください(例、2022-03):')

try:
    if int(order_count) > 100:
        raise StockError
    if card_number != '1111-1111-1111-1111':
        raise NumberError
    if expired_at != '2025-03':
        raise ExpiredError
    print('ご購入ありがとうございます')
except StoreErorr:
    print('在庫切れです')
except CardErorr as e:
    print('決済でエラーが発生しました')
    if isinstance(e, ExpiredError):
        print('有効期限が違います')
    elif isinstance(e, NumberError):
        print('カード番号が違います')
finally:
    print('またのご利用お待ちしています')
