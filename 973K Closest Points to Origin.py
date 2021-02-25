
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            if len(heap)<K:
                heapq.heappush(heap,[-(x*x+y*y),[x,y]])
                
            else:
                heapq.heappushpop(heap,[-(x*x+y*y),[x,y]])
        return [pair for value, pair in heap]

##accepted
# class Solution(object):
#     def kClosest(self, points, K):
#         points.sort(key = lambda P: P[0]**2 + P[1]**2)
#         return points[:K]

##accepted
# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
#         dis = []
#         out=[]
#         res=[]
#         f = 0
        
#         for i in range(len(points)):
#             dis.append(points[i][0]*points[i][0]+points[i][1]*points[i][1])
        
#         for i in dis:
#             if f<K:
#                 f+=1
#                 out.append(i)
#             else:
#                 tempmax = max(out)
#                 #idx =  out.index(tempmax)
#                 if i<tempmax:
#                     out.remove(tempmax)
#                     out.append(i)
        
#         for i in out:
#             idx = dis.index(i)
#             res.append([points[idx][0],points[idx][1]])
#             #avoid the same Euclidean distance in the dis, and get the wrong same point
#             points.remove(points[idx])
#             dis.remove(i)
        
#         return res
            
                    
                    
        
        