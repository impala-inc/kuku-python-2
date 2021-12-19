# x_4_3
#
# 「a」「b」「c」「d」がそれぞれどんな値となるかを予想してください

class MyStr(str):
    pass


a = 'こんにちは' == str('こんにちは')
b = 'こんにちは' == MyStr('こんにちは')
c = type('こんにちは') == type(str('こんにちは'))
d = type('こんにちは') == type(MyStr('こんにちは'))

# print(a)
# print(b)
# print(c)
# print(d)
