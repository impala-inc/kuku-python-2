# x_4_4
#
# 「a」「b」「c」「d」がそれぞれどんな値となるかを予想してください

class MyStr(str):
    pass


i = 'こんにちは'
j = str('こんにちは')
k = MyStr('こんにちは')
m = MyStr('こんにちは')

print(id(i))
print(id(j))
print(id(k))
print(id(m))

a = i is j
b = i is k
c = i is m
d = k is m

print(a)  # => idが同じなので同一のオブジェクト
print(b)  # => idが異なるので同一のオブジェクトではない
print(c)  # => idが異なるので同一のオブジェクトではない
print(d)  # => idが異なるので同一のオブジェクトではない
