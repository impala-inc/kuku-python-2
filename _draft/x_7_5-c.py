# x_7_5
#
#

import re

text_1 = 'ももさん'
text_2 = 'ももたろさん'

a = r'もも.*さん'
b = r'もも.+さん'

print(bool(re.match(a, text_1)))
print(bool(re.match(a, text_2)))
print(bool(re.match(b, text_1)))
print(bool(re.match(b, text_2)))
