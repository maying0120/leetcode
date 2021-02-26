from collections import defaultdict
import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
         
        cost = 0
        while len(sticks)>1:
            a= heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            cost+=(a+b)
            heapq.heappush(sticks,a+b)
        return cost
            

        
#tle       
#         cost=0
#         while len(sticks)>1:
#             a = min(sticks)
#             sticks.remove(a)
          
#             b = min(sticks)
#             sticks.remove(b)
#             sticks.append(a+b)
#             cost+=(a+b)
#         return cost
        
        
