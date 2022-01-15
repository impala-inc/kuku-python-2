# x_5_4
#
# 「damaged()」を「hello()」のようなOnitaijiMemberクラスのインスタンスメソッド（関数）に修正してください。

class OnitaijiMember:
    def __init__(self, name, hit_points):
        self.name = name
        self.hit_points = hit_points

    def hello(self):
        print('私の名前は' + self.name + 'です')


momotaro = OnitaijiMember('桃太郎', 1800)
momotaro.hello()


def damaged(character, point):
    character.hit_points -= point
    print(character.name + 'は' + str(point) + 'のダメージを受けた')
    print('残りHPは' + str(character.hit_points))


damaged(momotaro, 200)
