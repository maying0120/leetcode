from collections import Counter
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder = collections.defaultdict(int)
        res = 0
        for i in time:
            
            if i%60==0:
                res +=remainder[0]
            else:
                res += remainder[60-i%60]
            #since it need to be pair,so the following step should put at bottom
            remainder[i%60]+=1
      
        return res
  




# TLE
#         if len(time)==0:
#             return 0
        
#         for i in range(len(time)):
#             time[i] = time[i]%60
        
#         pair = 0
#         tnum=0
#         snum=0
        
#         time = sorted(time)
#         timecount  = collections.Counter(time)
        
#         for i in time:
#             if i<30 and (60-i) in time:
#                 pair+= timecount[60-i]
#             elif i==30:
#                 tnum+=1
#             elif i==0:
#                 snum+=1
#         print('time',time)
  
        
#         pair=pair+(tnum*(tnum-1))//2+(snum*(snum-1))//2
#         return pair
            
                
              
        
        
                
            