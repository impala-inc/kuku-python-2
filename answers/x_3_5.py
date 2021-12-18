# x_3_5
#
# mathモジュールからfloor関数を「kirisute」という名前でimportして切り捨て計算を行ってください

from statistics import mean as heikin
from math import floor as kirisute

data = [7, 4, 3, 9]

print(kirisute(heikin(data)))
