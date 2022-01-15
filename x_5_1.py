# x_5_1
#
# 「きじ」のデータを「HP: 1100」で作成してください

class OnitaijiMember:
    def __init__(self, name, hit_points):
        self.name = name
        self.hit_points = hit_points


momotaro = OnitaijiMember('桃太郎', 1800)
inu = OnitaijiMember('いぬ', 1300)
saru = OnitaijiMember('さる', 1400)

print(momotaro.name)
print(inu.hit_points)
