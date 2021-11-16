class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.recursiveCheck(nums,0,len(nums)-1)>=0
    
    
    def recursiveCheck(self,nums,start,end):
        if start==end:
            return nums[start]
        
        return max(nums[start]-self.recursiveCheck(nums,start+1,end),nums[end]-self.recursiveCheck(nums,start,end-1))