# x_4_9
#
# MyListクラスに最後の要素を返す「last()」とリストの長さを返す「length()」というメソッドを定義してください

class MyList(list):
    def length(self):
        return len(self)

    def first(self):
        return self[0]

    def last(self):
        return self[-1]


sneakers = MyList(['adidas', 'new balance', 'Nike', 'PUMA'])

print(sneakers.first())
print(sneakers.last())
print(sneakers.length())
