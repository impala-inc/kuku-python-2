# x_7_5
#
#

import re

shortest_pattern = r'も.+?さん'
longest_pattern = r'も.+さん'
text = 'もーもたろさんももたろさん'

print(re.match(shortest_pattern, text)[0])
print(re.match(longest_pattern, text)[0])
