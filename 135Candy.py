class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        res = [1 for i in range(len(ratings))]  
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                res[i] =res[i-1]+1
                
        for j in range(len(ratings)-2,-1,-1):  
    
            if ratings[j] > ratings[j+1]:
            #[1,3,4,5,2] 这种情况
                res[j] = max(res[j+1]+1,res[j])
                
        print('res',res) 
        return sum(res)