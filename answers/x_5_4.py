# x_5_4
#
# 「damaged()」を「hello()」のようなOnitaijiMemberクラスのインスタンスメソッド（関数）に修正してください。

class OnitaijiMember:
    def __init__(self, name, hit_points):
        self.name = name
        self.hit_points = hit_points

    def hello(self):
        print('私の名前は' + self.name + 'です')

    def damaged(self, point):
        self.hit_points -= point
        print(self.name + 'は' + str(point) + 'のダメージを受けた')
        print('残りHPは' + str(self.hit_points))


momotaro = OnitaijiMember('桃太郎', 1800)
momotaro.hello()

momotaro.damaged(200)
