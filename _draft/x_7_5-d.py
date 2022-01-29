# x_7_5
#
#

import re

text_1 = 'もーもたろさんももたろさん'
text_2 = 'ももたろさん'

a = r'も.*?さん'
result = re.findall(a, text_1)
print(result[0])
print(result[1])

# print(bool(re.match(a, text_1)))
# print(bool(re.match(a, text_2)))
# print(bool(re.match(b, text_1)))
# print(bool(re.match(b, text_2)))
