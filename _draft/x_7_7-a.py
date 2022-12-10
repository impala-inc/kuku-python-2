# x_7_7
#
#

import re


def is_match(pattern, pin):
    return bool(re.match(pattern, pin))


pin = '1234'  # 暗証番号

pattern1 = r'[0-9]{4}'
pattern2 = r'[2-9]{4}'
pattern3 = r'[0-9]{3}'
pattern4 = r'[0-9]{3, 5}'


print(is_match(r'[0-9]{4}', pin))
