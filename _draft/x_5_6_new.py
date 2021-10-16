# x_5_6
#
# 鬼鬼鬼鬼鬼
# 鬼鬼鬼鬼鬼
# 鬼い桃さ鬼
# 鬼鬼き鬼鬼
# 鬼鬼鬼鬼鬼

class OnitaijiMember:
    def __init__(self, name, gyou, retu):
        self.name = name
        self.gyou = gyou
        self.retu = retu


members = []
members.append(OnitaijiMember('桃太郎', 2, 2))
members.append(OnitaijiMember('いぬ', 2, 1))
members.append(OnitaijiMember('さる', 2, 3))
members.append(OnitaijiMember('きじ', 3, 2))

gyou = 0
while gyou < 5:
    retu = 0
    text = ''
    while retu < 5:
        member_name = ''
        for member in members:
            if gyou == member.gyou and retu == member.retu:
                member_name = member.name[0]
        if member_name != '':
            text += member_name
        else:
            text += '鬼'
        retu += 1
    print(text)
    gyou += 1
