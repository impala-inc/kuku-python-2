# x_1_7
#
# 日付を引数にとりその日が何曜日であるかを返す「get_weekday()」を定義してください。

import datetime

day = '2021-12-29'


def get_weekday(day):
    wday = ['月', '火', '水', '木', '金', '土', '日']
    date = datetime.datetime.strptime(day, '%Y-%m-%d')
    return wday[date.weekday()]


result = get_weekday(day)
print(result)
