class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if not prices or len(prices)==1:
            return 0
        start = prices[0]

        for i in range(len(prices)-1):
            if prices[i] > prices[i+1]:
                profit += (prices[i] -start)
                start = prices[i+1]              
      
            elif i+1==len(prices)-1:
                profit += (prices[i+1] -start)    
        return profit
                    
                