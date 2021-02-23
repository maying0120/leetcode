class Solution:
    def trap(self, height: List[int]) -> int:
       
	# // 思考过程：
	# // brute force: for each bar, how much water the water can be saved above this bar
	# // Math.min(leftmost larger than cur bar, rightmost larger than current bar)  - self height 
	# // time: O(n^2)
	# // 想想怎么降低时间复杂度， 看哪个部分是重复操作的，浪费了时间？对每个bar，我们都需要反复的往左右看，找比他大的bar
	# // 如果我们可以记录一下每个bar左右比他大的bar是哪个就好了
	# // 所以我们可以用两个array 分别记录左边大的bar，右边大的bar。这样，时间复杂度是O（n），空间复杂度是O（2n）-> O（n）
	# // 那现在来想想怎样才能降低空间复杂度呢
	# // 不用array来记录左边和右边最大的分别是多少，用两个pointer从左从右分别traverse，一边记录当前最大是多少
	# // 那我们就需要left, right两个pointer 和leftmax、rightmax两个variable
	# // 什么时候计算可以储存的水量呢？当leftmax < rightmax的时候，可以计算left上面储存的水量, right 同理
	# // 因为 right-1max >= rightmax ====> leftrightmax >= rightmax 而leftmax <= rightmax so leftmax <= leftrightmax
	# // 我们可以确定储存在cur left上的水量是由leftmax决定的    
        
        l,r= 0,len(height)-1
        leftmax,rightmax = 0,0
        water = 0
        
        while l<r:
            leftmax = max(leftmax,height[l])
            rightmax = max(rightmax,height[r])
            print('leftmax',leftmax)
            print('rightmax',rightmax)
            
            if leftmax < rightmax:
                water +=leftmax-height[l]
                l+=1
            else:
                water+=rightmax -height[r]
                r-=1
        return water
        
  
#         if len(height)<=1:
#             return 0
#         water=0
#         leftmax = [0]*len(height)
#         rightmax = [0]*len(height)
#         leftmax[0]=height[0]
#         rightmax[-1] =height[-1]
        
#         for i in range(1,len(height)):
#             leftmax[i] = max(height[i],leftmax[i-1])
            
#         for i in range(len(height)-2,0,-1):
#             rightmax[i] = max(height[i],rightmax[i+1])
        
#         for i in range(1,len(height)):
#             water += min(leftmax[i],rightmax[i])-height[i]
        
#         return water
