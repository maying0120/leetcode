class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #根据身高降序排列
        people = sorted(people, key =lambda x:(-x[0],x[1]))
        res=[]
        for p in people:
            #p[1] 代表当前比这个高的人的数量，作为index
            res.insert(p[1],p)
        return res
            
        
        