n = int(input())
sum=0
for i in range(1,n+1):
    n1 = int(input())
    n1 = ((-1)**(i-1))*n1
    sum +=n1
print(sum) 
