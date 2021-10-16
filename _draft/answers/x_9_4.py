# x_9_4
#
#

class MyStr(str):
    pass


class MyInt(int):
    pass


class MyList(list):
    pass


class MyDict(dict):
    pass


print(MyStr('あああ') + MyStr('いいい'))
print(MyInt(10) + MyInt(100))
print(MyList([1, 2, 3]) + MyList([1, 2, 3]))
print(MyDict({'a': 1, 'b': 2}) + MyDict({'c': 1, 'd': 2}))
