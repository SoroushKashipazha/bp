hands = [1,0,0,0,0,0]
remainChance=4
while True:
    quest = int(input("please choose a hand"))
    order = int(input("for gol inter 1 for poch inter 0"))
    remainChance -=1
    if order == 1 and hands[quest] == 1:
        print("you won!")
        break
    if order == 0 and hands[quest] == 1:
        print("you lost!")
        break
    if remainChance >0 and order == 0:
        if hands[quest]==0:
            hands.pop(quest)
