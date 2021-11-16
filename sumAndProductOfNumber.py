# your code goes here
n = int(input())
n1=n

sum = 0
product = 0

while(n!=0):
    if(n1==n):
        product=1
    s = n%10
    #print(s)
    sum = sum +s
    #print(sum)
    product = product * s
    #print(product)
    n = n//10

print(product)
print(sum)
print(product-sum)
