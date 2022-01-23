# x_4_5
#
# 「a」「b」「c」「d」がそれぞれどんな値となるかを予想してください

hello = 'Hello World'

print(hello.upper())
print(hello.lower())
print(hello.title())
print(hello.swapcase())


class MyStr(str):
    pass


sneaker_brands = MyStr('adidas Nike PUMA')

a = sneaker_brands.upper()
b = sneaker_brands.lower()
c = sneaker_brands.title()
d = sneaker_brands.swapcase()

print(a)  # => ADIDAS NIKE PUMA(strを継承しているためupper()が使える)
print(b)  # => adidas nike puma(strを継承しているためlower()が使える)
print(c)  # => Adidas Nike Puma(strを継承しているためtitle()が使える)
print(d)  # => ADIDAS nIKE puma(strを継承しているためswapcase()が使える)
