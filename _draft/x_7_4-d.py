# x_7_4
#
#

import re

pattern1 = r'\d\d\d-\d\d\d\d'
pattern2 = r'\d{3}-\d{4}'
pattern3 = r'[0-9]{3}-[0-9]{4}'

zipcode = input('郵便番号を入力してください(xxx-xxxx):')

if re.match(pattern1, zipcode):
    print('正しい郵便番号です')
else:
    print('不正な郵便番号です')

credit_card_number = input('カード番号してください(xxxx-xxxx-xxxx-xxxx):')
