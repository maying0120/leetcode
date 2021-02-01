class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0 
        r = len(nums)-1
        minval = nums[0]
        
        
        while l<r:
            #This is because you can't decide on which half of the array you could eliminate. For example [3,3.3.3,1,3] you could see that left, mid and right elements are same. Now you have to remove the duplicate from both ends until you have to find the range where the traditional binary search condition could be applied. This implies that you remove the duplicates from sorted array and do binary search on remaining elements. So the time complexity would become O(n).
            mid = l+(r-l)//2
            if nums[l]==nums[mid]==nums[r]:       
                l+=1
                r-=1
            elif nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid+1
        
        return nums[l]


#Case 1). nums[pivot] < nums[high]
#Case 2). nums[pivot] > nums[high]
#Case 3). nums[pivot] == nums[high]
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0 
        r = len(nums)-1        
        while l<r:
            mid = l +(r-l)//2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid+1
            else:
                r-=1
        
        return nums[l]
                
         
                
            