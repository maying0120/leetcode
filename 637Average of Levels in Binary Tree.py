# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        stack=[]
        ans=[]
        if root is None: 
            return ans
        stack.append(root)
           # print(stack)
        while stack != []:
            nextstack=[]
            tmp=[]
            for node in stack:
                tmp.append(node.val)
                if node.left:
                    nextstack.append(node.left)
                if node.right:
                    nextstack.append(node.right)
         
            ans.append(sum(tmp)/len(tmp))
            stack = nextstack
        return ans
          