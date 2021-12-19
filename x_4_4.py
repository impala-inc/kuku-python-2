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

# print(a)
# print(b)
# print(c)
# print(d)
