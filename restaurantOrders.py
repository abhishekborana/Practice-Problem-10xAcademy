totalOrders = int(input())
table= int(input())

orderList=[]
bill=[]

for i in range((totalOrders)):
    orderList.append(int(input()))
for i in range((totalOrders)):
    bill.append(int(input()))


finalBill=[]
loop=len(orderList)
i=0
while(i<loop):
    #print(i)
    if(i==(len(orderList)-1)):
        count1=0
    else:
        num=orderList[i]
        count1=orderList.count(num)
    if(count1>1):
        sum1=bill[i]+bill[orderList.index(orderList[i],i+1)]
        ind=orderList.index(orderList[i],i+1)
        #print(ind,sum1)
        finalBill.append(sum1)
        orderList.pop(ind)
        #print(orderList)
        loop = loop-1
    else:
        finalBill.append(bill[i])
    i=i+1

maxi = max(finalBill)

for i,val in enumerate(finalBill):
    if(maxi==val):
        print(orderList[i])

        
    