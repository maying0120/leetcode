class Solution:
    memo={}
    #不佳memo会超时
    def beautifulArray(self, N: int) -> List[int]:
        if N==1:
            return [1]
        if N in self.memo:
            return self.memo[N]
        
        odd = [i*2-1 for i in self.beautifulArray(N//2+N%2) ]
        even = [i*2 for i in self.beautifulArray(N//2)]
        self.memo[N] = odd+even
        
        return odd+even
 

#dp解法 从下到上
class Solution1:
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        dp = {}
        dp[1] = [1]
        for i in range(2,N+1):
            dp[i] = [x*2 for x in dp[i//2]] + [x*2-1 for x in dp[i-i//2]]
        
        return dp[N]
