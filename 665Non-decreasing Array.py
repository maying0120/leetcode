class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
 #  4(i) 2(i+1) 3 -> change i  big->small
 #  2 3 7(i) 1(i+1) 8()  -> change i+1 small->big
        count = 0
       
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count+=1
                if count>1:
                    return False
          
                if (i-1<0 or nums[i-1]<=nums[i+1]):
                    nums[i] = nums[i+1]
                else:
                    nums[i+1]= nums[i]
        
        return True
                    
        return count<=1