class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left = 0
        right = len(nums)-1
        
        while left+1<right:
            
            mid = left+(right-left)//2
            if nums[mid]==target:
                return True
            
            #因为数组存在重复数字，如果中点和左端的数字相同，我们并不能确定是左区间全部 相同，还是右区间完全相同。在这种情况下，我们可以简单地将左端点右移一位，然后继续进行
            elif nums[right] == nums[mid]:
                right-=1
            elif nums[left] == nums[mid]:
                left+=1
            
            elif nums[left] < nums[mid]:
                if nums[left]<=target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            elif nums[mid] < nums[right]:
                if nums[mid] <= target and target <=nums[right]:
                    left = mid
                else:
                    right = mid
        
        if nums[left]==target or nums[right]==target:
            return True
        else:
            return  False
        