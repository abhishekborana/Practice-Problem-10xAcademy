strng = input()
red=0
green=0
for i in strng:
    if(i=='R'):
        red+=1
    else:
        green+=1
print(min(red,green))