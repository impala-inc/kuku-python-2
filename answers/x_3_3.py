# x_3_3
#
# statistics.meanで計算した平均の値の小数低下を切り捨ててください

import statistics
import math

data = [7, 4, 3, 9]

print(math.floor(statistics.mean(data)))
