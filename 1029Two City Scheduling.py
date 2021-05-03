class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        arr=[]
        for c in range(len(costs)):
            arr.append([c,costs[c][0]-costs[c][1]])
        res=0
        arr = sorted(arr,key=lambda x:x[1])
        n=len(arr)
        half = n/2-1
        
        for i in range(n):
            if i<=half:
                res+=abs(costs[arr[i][0]][0])
            else:
                res+=abs(costs[arr[i][0]][1])
        return res
            
     
        #[[10,20],[30,200],[400,50],[20,35]]
        #[-10,-170,350,-15]  sort->[-170,-15,-10,350]