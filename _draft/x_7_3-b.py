# 7の段「正規表現 ~ 3」
#
# クレジットカードの番号を判定するコードを追加してください

import re

zipcode = input('郵便番号を含む文字を入力してください(xxx-xxxx):')

if re.search(r'^[0-9]{3}-[0-9]{4}$', zipcode):
    print('正しい郵便番号です')
elif re.search(r'[0-9]{3}-[0-9]{4}', zipcode):
    print('正しい郵便番号が含まれています')
else:
    print('郵便番号は含まれていません')

credit_card_number = input('クレジットカード番号を入力してください(xxxx-xxxx-xxxx-xxxx):')
