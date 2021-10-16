# x_5_8
#
#

from mypackage.janken import Janken

my_hand = Janken()
your_hand = Janken()

print('自分の手は' + my_hand.hand)
print('相手の手は' + your_hand.hand)

if my_hand == your_hand:
    print('あいこ')
elif my_hand > your_hand:
    print('勝ち')
else:
    print('負け')
