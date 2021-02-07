class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def rec(ans,temp,start):
            if len(temp)==k:
                ans.append(temp)
            for i in range(start,n+1):
                rec(ans,temp+[i],i+1)
        
        ans =[]
      
        rec(ans,[],1)
        return ans
            
        