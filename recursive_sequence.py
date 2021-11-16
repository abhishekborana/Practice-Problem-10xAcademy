def seq(n):
    if n==1:
        return 1
    term =1
    s=((n-1)*(n))//2 +1
    e=s+n
    for i in range(s,e):
        term*=i
    return seq(n-1)+term
t=int(input())
for i in range(t):
    print(seq(int(input())))