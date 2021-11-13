# x_2_3
#
# 「a」「b」「c」「d」がそれぞれどんな値となるかを予想してください

def kuku(a=9, b=9):
    return a * b


a = kuku(6, 8)  # => 48(6 * 8)
b = kuku()  # => 81(9 * 9)
c = kuku(3)  # => 27(3 * 9)
d = kuku(b=4)  # => 36(9 * 4)

# print(a)
# print(b)
# print(c)
# print(d)
