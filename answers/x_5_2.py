# x_5_2
#
# 桃太郎のHPを300減らしてください。

class OnitaijiMember:
    def __init__(self, name, hit_points):
        self.name = name
        self.hit_points = hit_points


momotaro = OnitaijiMember('桃太郎', 1800)

print(momotaro.name + 'は300のダメージを受けました')
momotaro.hit_points -= 300

print(momotaro.hit_points)
