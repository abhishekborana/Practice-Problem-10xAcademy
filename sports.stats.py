size=int(input())
sports={}
for i in range(size):
    name,sport=input().split()
    if(sport not in sports):
        sports[sport]=1
    else:
        sports[sport]+=1
print(max(sports, key=sports.get))
print(sports[football])
    