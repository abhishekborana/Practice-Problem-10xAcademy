symbol = input()
res = 0
for i in range(0,len(symbol)):
    if(symbol[i]=="+"):
        res += 1
    else:
        res -= 1
print(res)