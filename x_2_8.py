# x_2_8
#
# func_a() ~ func_d()の関数を一つにまとめてfunc_x(5)を実行すると「5 * 4 * 3 * 2 * 1」を返すように修正してください
# ヒント: 関数の中から自分自身の関数を呼び出します

def func_a(n):
    return n * 1


def func_b(n):
    return n * func_a(n - 1)


def func_c(n):
    return n * func_b(n - 1)


def func_d(n):
    return n * func_c(n - 1)
