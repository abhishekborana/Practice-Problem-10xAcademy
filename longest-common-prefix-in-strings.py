class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r=float("inf")
        for i in strs:
            if(r>len(i)):
                r=len(i)
        res=[]
        for i in strs:
            res.append(i[:r])
        o=0
        ans=""
        for i in range(len(res[0])):
            m=set()
            for j in range(len(res)):
                m.add(res[j][o])
            o+=1    
            if(len(m)==1):
                m=list(m)
                ans+=m[0]
            else:
                break
        return ans