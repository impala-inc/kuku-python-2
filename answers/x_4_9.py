# x_4_9
#
# MyListクラスに最後の要素を返す「last()」とリストの長さを返す「length()」というメソッドを定義してください

class MyList(list):
    def first(self):
        return self[0]

    def last(self):
        return self[-1]

    def length(self):
        return len(self)


sneaker_brands = MyList(['adidas', 'new balance', 'Nike', 'PUMA'])

print(sneaker_brands.first())
print(sneaker_brands.last())
print(sneaker_brands.length())
