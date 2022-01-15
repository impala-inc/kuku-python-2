# x_5_5
#
# 桃太郎(Human)と同じようにOnitaijiMemberを継承して「Dog、Monkey、Bird」の3つのクラスを作り
# 「犬は噛みつきました」「さるは引っ掻きました」「きじ はくちばしで突きました」と表示してください

class OnitaijiMember:
    def __init__(self, name, hit_points):
        self.name = name
        self.hit_points = hit_points


class Human(OnitaijiMember):
    def attack(self):
        print(self.name + 'は刀で斬りかかりました')


class Dog(OnitaijiMember):
    def attack(self):
        print(self.name + 'は噛みつきました')


class Monkey(OnitaijiMember):
    def attack(self):
        print(self.name + 'は引っ掻きました')


class Bird(OnitaijiMember):
    def attack(self):
        print(self.name + 'はくちばしで突きました')


members = []

members.append(Human('桃太郎', 1800))
members.append(Dog('いぬ', 1300))
members.append(Monkey('さる', 1400))
members.append(Bird('きじ', 1400))

for member in members:
    member.attack()
