# x_7_9
#
#

import re

members = [
    {'name': '田中', 'food': 'オムライス'},
    {'name': '山本', 'food': 'ラーメン'},
    {'name': '吉田', 'food': 'お寿司'},
    {'name': '石田', 'food': 'カレーライス'},
    {'name': '東野', 'food': 'ハヤシライス'},
    {'name': '東野', 'food': 'カレーパン'},
]

pattern = r'(カレー|ハヤシ|オム)ライス'

for member in members:
    if re.match(pattern, member['food']):
        print(member['name'])
