# x_7_5
#
#

import re

text_a = 'もさん'
text_b = 'ももさん'
text_c = 'ももたろさん'
text_d = 'もーもたろさんももたろさん'

a = r'も.*さん'
b = r'も.+さん'
c = r'も.*?さん'
d = r'も.+?さん'

print(bool(re.match(a, text_a)))
print(bool(re.match(b, text_b)))
print(bool(re.match(c, text_c)))
print(bool(re.match(d, text_d)))
