currPoints = int(input())

f=1
while(f):
    userChoice = int(input("Enter game choice"))
    if(userChoice==1 and currPoints>=10):
        print("Thanks for Playing Rock climbing")
        currPoints -=10
    elif(userChoice==2 and currPoints>=30):
        currPoints -=30
        print("Thanks for Playing Dirt Biking")
    elif(userChoice==3 and currPoints>=50):
        currPoints -=50
        print("Thanks for Playing PaintBall")
    elif(userChoice==4 and currPoints>=50):
        currPoints -=50
        print("Thanks for Playing Shooting")
    elif(userChoice>4 or userChoice<1):
        print("None Game Exist Try Again !")
    else:
        print("sorry ! In Sufficient Points "+str(currPoints))
        f=0
    