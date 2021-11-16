testCase =int(input())
income=[]
sum=0
mem=0
for i in range(testCase):
    currenIncome=int(input())
    income.append(currenIncome)
for i in range(testCase):
    members=int(input())
    if(members>2):
        sum+=income[i]
        mem+=1
print(sum//mem)

    