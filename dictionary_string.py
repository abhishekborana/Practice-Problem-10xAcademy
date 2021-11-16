def stringCheck(mainStr,subStrList):
    for curStr in subStrList:
        start=0
        for i in range(len(mainStr)):
            if(curStr[start]==mainStr[i]):
                start+=1
            if(start==len(curStr)):
                return len(curStr)
    return 0


mainStr=input()
subStrList=input().split()

subStrList.sort(key=lambda x:-len(x))
#print(subStrList,subStr)
print(stringCheck(mainStr,subStrList))