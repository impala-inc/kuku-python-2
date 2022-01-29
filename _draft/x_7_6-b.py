# x_7_6
#
#

import re

pattern = r'も+'

print(re.search(pattern, 'すもももももももものうち'))

onis = '赤鬼青鬼黄鬼'
print(re.search(r'(.鬼)+', onis)[1])
