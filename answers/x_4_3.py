# x_4_3
#
# 「a」「b」「c」「d」がそれぞれどんな値となるかを予想してください

class MyStr(str):
    pass


a = 'こんにちは' == str('こんにちは')
b = 'こんにちは' == MyStr('こんにちは')
c = type('こんにちは') == type(str('こんにちは'))
d = type('こんにちは') == type(MyStr('こんにちは'))

print(a)  # => True(文字列同士を比較しているため)
print(b)  # => True(文字列同士を比較しているため)
print(c)  # => True(オブジェクトの型がどちらもstrのため)
print(d)  # => False(オブジェクトの型strとMyStrで異なるため)
