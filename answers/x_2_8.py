# x_2_8
#
# func_x(5)を実行すると「5 * 4 * 3 * 2 * 1」を返すように修正してください

def func_x(n):
    if n == 1:
        return n * 1
    else:
        return n * func_x(n - 1)


a = func_x(5)  # => 120

print(a)
