testCase = int(input())
for i in range(testCase):
    max,seat = map(int,input().split())
    if(max<seat):
        print("Invalid")
    elif(seat%8==1 or seat%8==4):
        print("L")
    elif(seat%8==2 or seat%8==5):
        print("M")
    elif(seat%8==3 or seat%8==6):
        print("U")
    elif(seat%8==0):
        print("SU")
    else:
        print("SL")