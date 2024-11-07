import random

sjb = ["石头","剪刀","布"]
a = (random.choice(('石头','剪刀','布')))
computer = a
player = input('请出拳: ')

print("您出的是: %s, AI玩家出的是: %s" % (player, computer))
if player == '石头':
    if a ==  '石头':
        print('平局')
    elif a == '布':
        print('输了')
    else:
        print ('胜利')

if player == '剪刀':
    if a ==  '剪刀':
        print('平局')
    elif a == '布':
        print('获胜')
    else:
        print ('输了')

if player == '布':
    if a ==  '布':
        print('平局')
    elif a == '石头':
        print('获胜')
    else:
        print ('输了')

