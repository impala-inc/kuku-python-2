# x_2_5
#
# 関数内で定義された変数や関数の引数はそのプロック内でのみ参照できる「ローカル変数」となり「locals()」関数でその内容を確認できます
# 「a」「b」「c」「d」がそれぞれどんな値となるかを予想してください

def sample(name):
    food = 'オムライス'
    print(locals())


sample('田中')


def full_name_a(first_name, last_name):
    a = locals()
    print(a)  # => {'first_name': '山田', 'last_name': '太郎'}


def full_name_b(first_name, last_name):
    first_name = '山中'
    b = locals()
    print(b)  # => {'first_name': '山中', 'last_name': '太郎'}


def full_name_c(first_name):
    c = locals()
    print(c)  # => {'first_name': '山口'}


def full_name_d():
    d = locals()
    print(d)  # => {}


first_name = '山田'
last_name = '太郎'

full_name_a(first_name, last_name)

full_name_b(first_name, last_name)

full_name_c('山口')

last_name = '二郎'

full_name_d()
