# x_7_7
#
#

import re


def is_not_valid(password):
    if re.match(r'[^0-9a-zA-Z]{8, 20}', password):
        print('8文字以上20文字以下の英数字を使用してください')
        return True

    return False


password = input('パスワードを設定してください(8文字以上20文字以下の英数字):')

if is_not_valid(password):
    print('パスワードは8文字以上の英数字にしてください')
else:
    print('パスワードを設定しました')
