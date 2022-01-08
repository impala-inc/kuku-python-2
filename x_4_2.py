# x_4_2
#
# 「a」「b」「c」「d」がそれぞれどんな値となるかを予想してください

class MyStr(str):
    pass


class MyInt(int):
    pass


class MyList(list):
    pass


class MyDict(dict):
    pass


a = MyStr('田中') + MyStr('太郎')
b = MyInt(200) + MyInt(100)
c = MyList(['桃太郎', 'いぬ']) + MyList(['かに', 'くり'])
d = MyDict(blue='青', yellow='黄', red='赤')

# print(a)
# print(b)
# print(c)
# print(d)
