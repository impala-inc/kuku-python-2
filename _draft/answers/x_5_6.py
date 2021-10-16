# x_5_6
#
# 「damaged()」を「hello()」のようなクラスのインスタンスメソッド（関数）に修正してください。

class Character:
    def __init__(self, name, hit_points, attack):
        self.name = name
        self.hit_points = hit_points
        self.attack = attack

    def hello(self):
        print('初めまして私の名前は' + self.name + 'です')

    def damaged(self, val):
        self.hit_points -= val
        print(self.name + 'は' + str(int(val)) + 'のダメージを受けた')
        print('残りHPは' + str(self.hit_points))


momotaro = Character('桃太郎', 1800, 220)
momotaro.damaged(200)
