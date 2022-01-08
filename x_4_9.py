# x_4_9
#
# MyListクラスに最後の要素を返す「last()」とリストの長さを返す「length()」というメソッドを定義してください

class MyList(list):
    def first(self):
        return self[0]


sneakers = MyList(['adidas', 'new balance', 'Nike', 'PUMA'])

print(sneakers.first())
