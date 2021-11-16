

for _ in range(int(input())):
    N,M,Q=map(int,input().split())
    x=set()
    y=set()
    x.add(N)
    y.add(M)
    x.add(1)
    y.add(1)
    for _ in range(Q):
        xCor,yCor=map(int,input().split())
        x.add(xCor)
        y.add(yCor)
    region=(len(x)-1)*(len(y)-1)
    x=list(x)
    y=list(y)
    x.sort(reverse=True)
    y.sort(reverse=True)
    miniX=float("inf")
    maxiX=float("-inf")
    miniY=float("inf")
    maxiY=float("-inf")
    for i in range(len(x)-1):
        maxiX=max(maxiX, x[i]-x[i+1])
        miniX=min(miniX, x[i]-x[i+1])
    for i in range(len(y)-1):
        maxiY=max(maxiY, y[i]-y[i+1])
        miniY=min(miniY, y[i]-y[i+1])
    mini=miniX*miniY
    maxi=maxiX*maxiY
    print(region,mini,maxi)


