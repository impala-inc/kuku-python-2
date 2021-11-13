# x_2_4
#
# 「a」「b」「c」「d」がそれぞれどんな値となるかを予想してください

def full_name_a(first_name, last_name):
    a = first_name + last_name
    print(a)  # => 山田太郎（姓名ともに引数から）


def full_name_b(first_name, last_name):
    first_name = '山中'
    b = first_name + last_name
    print(b)  # => 山中太郎（姓は関数内で上書きされたため）


def full_name_c(first_name):
    c = first_name + last_name
    print(c)  # => 山口太郎（姓は引数、名は関数外の変数の値を参照した）


def full_name_d():
    d = first_name + last_name
    print(d)  # => 山口太郎（姓名ともに関数外の変数の値を参照した）


first_name = '山田'
last_name = '太郎'

full_name_a(first_name, last_name)

full_name_b(first_name, last_name)

full_name_c('山口')

last_name = '二郎'

full_name_d()
