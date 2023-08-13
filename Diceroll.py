import random
print("\n\t press Enter to roll thr Dice : ")
f = input()
while True:
    a = random.randint(1,6)
    print(f"\n\t You Got {a}!!!")
    f = input("\n\n you want to roll again(y/n)?? ")
    if f=='y':
        continue
    else:
        print("\n\t\t THANK YOU FOR PLAYING!!! \n")
        break
    