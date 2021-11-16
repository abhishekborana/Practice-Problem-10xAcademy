
def bestScore(A,B,C):
       # complete the function
       A.sort()									#1 2 3 5  
       B.sort()									#1 2 4 8
       C.sort()									#5 6 6 9
       a,b,c=0,0,0
       res=float("inf")
       while(a<len(A) and b<len(B) and c<len(C)):
           cA=A[a]								#1					2        2			3			3			5	
           cB=B[b]								#1					1		 2			2			4			4
           cC=C[c]								#5					5		 5			5			5			5
           #|Tmax-Tmid|+|Tmid-Tmin|	
           currThreeNums=[cA,cB,cC]						
           maxi=max(currThreeNums)				#5					5		 5			5			5			5	
           mini=min(currThreeNums)				#1					1		 2			2			3			4
           mid=cA+cB+cC-maxi-mini				#1					2		 2			3			4			5
           curRes=abs(maxi-mid)+abs(mid-mini)	#5-1 + 1-1 = 4		5-1+2-1	 5-2+2-2	5-3+3-2		5-4+3-4		5-4+4-5
           res=min(curRes,res)					#4					4		 3			3			2			2
           print(curRes,res)					#4 ,4				4,4		 3,3		3,3			2,2
           if(mini==cA):
               a+=1								#a=1				a=1		 a=2		a=2			a=3
           elif(mini==cB):
               b+=1								#b=0				b=1		""			b=2     	b=2
           else:			
               c+=1								#c=0				c=0      ""			c=0			c=0
       print(res)
#DO not edit anything below this line

# Driver code 
A= [int(x) for x in input().split()] 
B= [int(x) for x in input().split()]  
C= [int(x) for x in input().split()]  
bestScore(A,B,C)