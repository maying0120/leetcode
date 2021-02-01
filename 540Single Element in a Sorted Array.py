class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        while l<r:
            mid = l+(r-l)//2
            length = l-mid+1
            
            if nums[mid]==nums[mid+1]:
                if length%2!=0:
                    l=mid+2
                else:
                    r = mid-1
            elif nums[mid] == nums[mid-1]:
                if length%2==0:
                    l  = mid+1
                else:
                    r  = mid-2
            else:
                return nums[mid]
        return nums[l]
                    
                