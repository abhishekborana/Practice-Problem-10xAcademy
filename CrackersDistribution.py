nCrackers , totUser = input().split()
nCrackers , totUser = int(nCrackers),int(totUser)
if(nCrackers ==0 or totUser==0):
    print("0")
else:
    if((nCrackers/totUser*100)<200):
        even = 1 + (nCrackers//totUser)
    else:
        even = (nCrackers//totUser)
    n=0
    highest =0
    for i in range(totUser):
        if(i==totUser-1):
            highest=nCrackers-n
        n += even
    if((nCrackers//totUser*100)<200):
        print(even-highest)
    else:
        print(highest-even)

    
