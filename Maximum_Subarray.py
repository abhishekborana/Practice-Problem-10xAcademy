class Solution:
    def maxSubArray(self,nums):
        res=float("-inf")
        curr_max=0
        for i in nums:
            curr_max=curr_max+i
            if(res<curr_max):
                res=curr_max
            if(curr_max<0):
                curr_max=0
        return res
            
sol=Solution()
testCases=[
    [-2,1,-3,4,-1,2,1,-5,4],
    [1],
    [5,4,-1,7,8],
    [-1,-5,-2,-8,-9,-10,-45,-1],
    [-1,-5,-2,-8,-9,10,-45,-1]
]
for i in testCases:
    res=sol.maxSubArray(i)
    print(res)
