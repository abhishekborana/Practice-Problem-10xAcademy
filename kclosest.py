def kClosest(points, k):
        res=[]
        for i in range(len(points)):
            m=((points[i][0])**2+(points[i][1]**2))**0.5
            res.append([m,[points[i][0],points[i][1]],points[i][0]+points[i][1]])
        
    
        res.sort(key=lambda x:x[0])
        print(res)
        m=[]
        for i in range(k):
            m.append(res[i][1])
        return m
print(kClosest(

[[-5,4],[-3,2],[0,1],[-3,7],[-2,0],[-4,-6],[0,-5]],6))