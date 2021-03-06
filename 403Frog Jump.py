class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        if not stones or (stones[1]-stones[0])!=1: 
           
            return False
        target = stones[-1]
        
        memo=set()
        #memo=[] tle?
        
        def dp(stones,cur,speed,target):
            if (cur,speed) in memo: 
                return False
            
            memo.add((cur,speed))
#print(memo)
            
            if cur==target: return True
            
            if cur>target or cur<0 or speed<=0 or cur not in stones:
                return False
            sp = [speed-1,speed,speed+1]
            
            for s in sp:
                if cur+s in stones:
                    if dp(stones,cur+s,s,target):
                        return True
            return False
                    
        res = dp(stones, 1, 1, target)
        return res
        