instruct=int(input())
instList=[]
bulb=0
con=0
for i in range(instruct):
    instList.append(input())
for i in instList:
    if(i=="ON"):
        if(bulb==0):
            con+=1
            bulb=1
        else:
            bulb=1
    elif(i=="OFF"):
        bulb=0
    else:
        if(bulb==0):
            bulb=1
            con+=1
        else:
            bulb=0
print(con)
    