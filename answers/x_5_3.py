# x_5_3
#
# 「私のHPはXXです」と自分のHPを表示する関数「my_hp()」を追加してください

class OnitaijiMember:
    def __init__(self, name, hit_points):
        self.name = name
        self.hit_points = hit_points

    def hello(self):
        print('私の名前は' + self.name + 'です')

    def my_hp(self):
        print('私のHPは' + str(self.hit_points) + 'です')


momotaro = OnitaijiMember('桃太郎', 1800)
momotaro.hello()
momotaro.my_hp()
