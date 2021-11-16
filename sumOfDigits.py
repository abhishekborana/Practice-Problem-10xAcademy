testCase = int(input())
res = 0
for i in range(testCase):
    n1 = input()
    sum=0
    product=1
    for i in n1:
        sum+=int(i)
        product*=int(i)
    if(sum>=product):
        res+=1
print(res) 