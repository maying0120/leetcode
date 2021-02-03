# reference https://jacobhuang91.github.io/all-in-one/leetcode/215.%20Kth%20Largest%20Element%20in%20an%20Array.html
#return heapq.nlargest(k, nums)[-1] one line solution
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums is None or len(nums)==0:
            return 0
        l = 0
        r = len(nums)-1
        while(1):
            pos = self.position(nums,l,r)
            if pos+1==k:
                return nums[pos]
            elif pos+1>k:
                r = pos-1
            else:
                l= pos+1
    
    def position(self,nums,left,right):
        piv = nums[left]
        l = left+1
        r = right
        while l<=r:
            if nums[l] < piv and nums[r] > piv:
                self.swap(nums,l,r)
                l+=1
                r-=1
            if nums[l]>=piv: l+=1
            if nums[r]<=piv: r-=1
        self.swap(nums,left,r)
        return r
    
    def swap(self,nums,left,right):
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp

        