class Solution:
    def rekursive(self, nums, path, ans):
        if len(nums) == 0:
            ans.append(path)
        else:
            for i in range(len(nums)):
                print('path',path)
                
                self.rekursive(nums[:i] + nums[i + 1:], path + [nums[i]], ans)

        return ans

    def permute(self, nums):
        res = self.rekursive(nums, [], [])
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visted = set()
        res = []
        self.backtrack(res,visted,[],nums)
        
        return res
        
    
    def backtrack(self,res,visted,subset,nums):
        
        if len(subset) == len(nums):
            res.append(subset)
        
        for i in range(len(nums)):
            if i not in visted:
                visted.add(i)
               # print('111v',subset)
                self.backtrack(res,visted,subset+[nums[i]],nums)
                
                visted.remove(i)
        