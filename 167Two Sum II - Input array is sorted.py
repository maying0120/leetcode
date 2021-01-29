

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        res = []
        
        dic ={}
        
        for i,j in enumerate(numbers):
            dic[j]= i+1 
        
        
        
        for i,j in enumerate(numbers):
            temp= target- j 
            if temp in numbers:
                res.append(i+1)
                res.append(dic[temp])
                break
        return res


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start  = 0
        end = len(numbers)-1
        
        ans=[]
        
        while start<=end:
            if numbers[start] + numbers[end]==target:
                ans.append(start+1)
                ans.append(end+1)
                return ans
            elif numbers[start] + numbers[end] < target:
                start+=1
            
            else:
                end-=1