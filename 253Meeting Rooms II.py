import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        
        
        # sort the intervals arrays by the start time
        #[0,30]->[5,10]->[15,20] 
        #[2,4]->[7,10]
        # [5,10]->[7,12]->[11,15]->[13,14]
        
        room = []
        intervals = sorted(intervals, key=lambda x:x[0])
        heapq.heappush(room,intervals[0][1])
        
        for i in intervals[1:]:
            if room[0] <= i[0]:
                heapq.heappop(room)
 
            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.               
            heapq.heappush(room,i[1])
        return len(room)
             
    