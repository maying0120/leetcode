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
        