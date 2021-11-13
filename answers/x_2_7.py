# xx_2_7
#
# 「a」「b」「c」「d」がそれぞれどんな値となるかを予想してください

def func_a(n):
    return n * 1


def func_b(n):
    return n * func_a(n - 1)


def func_c(n):
    return n * func_b(n - 1)


def func_d(n):
    return n * func_c(n - 1)


a = func_a(1)  # => 1(1 * 1)
b = func_b(2)  # => 2(2 * 1)
c = func_c(3)  # => 6(3 * 2 * 1)
d = func_d(4)  # => 24(4 * 3 * 2 * 1)

# print(a)
# print(b)
# print(c)
# print(d)
