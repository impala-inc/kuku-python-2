# x_6_6
#
# number_of_peopleにマイナスの値が入力された時にMinusErrorを発生させてください

class MinusError(Exception):
    pass


total_price = 4000
number_of_people = input('合計で4000円です。何人でお支払いされますか？:')

try:
    price = total_price // int(number_of_people)
    print('お一人あたり' + str(price) + '円のお支払いになります')
except Exception as e:
    if isinstance(e, ValueError):
        print('ValueError。数字を入力してください')
