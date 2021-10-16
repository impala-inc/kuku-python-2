# x_9_5
#
#

class MyStr(str):
    def star(self):
        return '✰⋆*' + self + '*⋆✰'

    def sun(self):
        return '✹' + self + '✹'

    def moon(self):
        return '☽' + self + '☽'

    def kirakira_print(self, _type):
        if _type == '太陽':
            return self.sun()
        elif _type == '月':
            return self.moon()
        elif _type == '星':
            return self.star()
        else:
            return self


my_str = MyStr('やっほー')
print(my_str.kirakira_print('太陽'))
