# x_4_7
#
# 「a」「b」「c」「d」がそれぞれどんな値となるかを予想してください

hello = 'Hello World'

print(hello.upper())
print(hello.lower())
print(hello.title())
print(hello.swapcase())


class MyStr(str):
    def upper(self):
        return '<大文字にします>' + super().upper()

    def lower(self):
        return '<小文字にします>' + super().lower()

    def title(self):
        return '<題名っぽくします>' + super().title()

    def swapcase(self):
        return '<大文字と小文字を反転させます>' + super().swapcase()


sneakers = MyStr('adidas Nike PUMA')

a = sneakers.upper()
b = sneakers.lower()
c = sneakers.title()
d = sneakers.swapcase()

# print(a)
# print(b)
# print(c)
# print(d)
