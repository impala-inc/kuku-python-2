# x_2_3
#
# q_1 ~ q_4がそれぞれどんな値となるかを予想してください

from module import qa


def kuku(a=9, b=9):
    return a * b


q_1 = kuku(6, 8)
q_2 = kuku()
q_3 = kuku(3)
q_4 = kuku(b=4)


# ここはとりあえず無視
qa.execute(locals())
