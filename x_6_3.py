# 6の段「エラーと例外処理 ~ 3」
#
# 必ず「おわり」まで表示できるようにコードを修正してください

import random


class MyError(Exception):
    pass


class FooError(MyError):
    pass


class BarError(MyError):
    pass


class BazError(MyError):
    pass


try:
    result = random.choice(['foo', 'bar', 'baz'])
    if result == 'foo':
        raise FooError
    elif result == 'bar':
        raise BarError
    else:
        raise BazError
except FooError:
    print('FooError、BarError、BazErrorを無視します')


print('おわり')
