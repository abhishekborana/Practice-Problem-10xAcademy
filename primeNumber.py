testCase = int(input())


for i in range(testCase):
    ans = "Yes"
    n1 = int(input())
    for i in range(2,n1):
        if(n1%i==0):
            ans = "No"
            break
    print(ans) 




