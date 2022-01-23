# x_7_2
#
#

import re


text = '2022年レノファ山口はJ2リーグで優勝を目指します'

pattern = 'い'
str = input('ひらがなの「い」のつく言葉を入力してください:')

print(re.sub(pattern, 'ﾚヽ', str))
