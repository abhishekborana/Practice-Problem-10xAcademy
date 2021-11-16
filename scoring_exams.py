# your code goes here
size,query=map(int,input().split())
timeA=list(map(int,input().split()))
marksA=list(map(int,input().split()))
timeA.sort(reverse=True)
time_per_ith=[timeA[0]]
for i in range(1,size):
    time_per_ith.append(time_per_ith[-1]+timeA[i])
for i in range(query):
    no_of_ques=int(input())
    print(time_per_ith[no_of_ques-1])
