class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        total = len1+len2
        i,j = 0,len1
        if len1 > len2:
            return self.findMedianSortedArrays(nums2,nums1)
        
        #nums1=[1,4,5]
        #nums = [2,3]  sort->[1,2,3,4,5] 5+1//2=3  cuta=(0+2-1)//2=0  cutb=3
        
        print('here')
        while i<=j:
            cuta = i +(j-i)//2    
    
            #
            cutb = (total+1)//2 - cuta
            
            # make sure len(left)==left(right) also the max value of left part is <= than the min value of the right part
            if cuta<len1 and nums2[cutb-1]>nums1[cuta]: 
                i=cuta+1
       
            elif cuta>0 and nums1[cuta-1] > nums2[cutb]: 
                j=cuta-1
              
           
            
            else:
               
                if cuta==0:   maxleft = nums2[cutb-1]
                elif cutb==0: maxleft = nums1[cuta-1]
                else:maxleft=max(nums1[cuta-1],nums2[cutb-1])
                print('test')
                
                if (len1+len2)%2==1:
                    return maxleft
                if cuta==len1: minright = nums2[cutb]
                elif cutb==len2: minright = nums1[cuta]
                else: minright = min(nums1[cuta],nums2[cutb])
                return (maxleft+minright)/2
                    
            
                