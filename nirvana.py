import bisect
n, k = map(int,input().split())
a = sorted(list(map(int,input().split())))
 
def test(x):
    i = 0
    z = k
    while i < n:
        z -= 1
        if z < 0:
            return False
        i = bisect.bisect(a, a[i] + x * 2)
    return True
    
lo, hi = 0, a[-1] - a[0]
while lo < hi:
    x = (lo + hi) / 2
    if test(x):
        hi = x
    else:
        lo = x + 1
print(int(lo))