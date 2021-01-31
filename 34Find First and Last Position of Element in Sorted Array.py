class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:        
        def findleft(nums,target):
        
            l = 0
            r =len(nums)-1
            
        
            while l+1<r:
                mid  = l+(r-l)//2
                if nums[mid]>=target:
                    r = mid
                else:
                    l = mid
            
            if nums[l]==target:
                return l
            elif nums[r]==target:
                return r
            else:
                return -1

        
        def findright(nums,target):
        
            l = 0
            r =len(nums)-1
            #注意这里必须是l+1<r, 
            while l+1<r:
                mid  = l+(r-l)//2
                if nums[mid]<=target:
                    l =mid
                else:
                    r = mid
            
            if nums[r]==target:
                return r
            elif nums[l]==target:
                return l
            else:
                return -1
            
        if nums is None or len(nums)==0: return [-1,-1]
        left = findleft(nums,target)
        right = findright(nums,target)
        return [left,right]
            