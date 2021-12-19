# x_4_8
#
# 「MyStr」を継承したクラス「MyStr2」を作成して「upper()」と「lower()」の結果を入れ替えてください

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
