# x_6_7
#
#

class CardEror(Exception):
    pass


class NumberError(CardEror):
    pass


class ExpiredError(CardEror):
    pass


card_number = input('カード番号を入力してください(例、0000-0000-0000-0000):')
expired_at = input('有効期限を入力してください(例、2022-03):')

try:
    if card_number != '1111-1111-1111-1111':
        raise NumberError('カードナンバーが違います')
    if expired_at != '2025-03':
        raise NumberError('有効期限が違います')
except CardEror:
    print('カードエラーです')
