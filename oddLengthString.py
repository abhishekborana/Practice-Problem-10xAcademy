testCase = int(input())
res=0
for i in range(testCase):
    n1 = input()
    if(len(n1)%2!=0):
        res+=1
print(res)