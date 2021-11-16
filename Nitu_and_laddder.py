size=int(input())

for row in range(size+1):
    for col in range(size-row):
        print(" ",end='')
    for col in range(row):
        print("#",end='')
    print()
        