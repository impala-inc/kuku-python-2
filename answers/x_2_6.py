# x_2_6
#
#　問題を準備中です

first_name = '山田'
last_name = '太郎'
members = ['桃太郎', 'いぬ', 'さる', 'きじ']
fruits = {'apple': 'りんご', 'banana': 'バナナ'}


def change_first_name():
    global first_name
    first_name = '山村'


def change_last_name():
    last_name = '四郎'


def change_list():
    members[2] = 'ゴリラ'


def change_dict():
    fruits['grape'] = 'ぶどう'


change_first_name()
change_last_name()
change_list()
change_dict()


def print_global_variables():
    print(first_name + last_name)
    print(members)
    print(fruits)


print_global_variables()
