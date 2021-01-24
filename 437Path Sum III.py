# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count=0
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.recur(root,sum)
        return self.count
        
        
            
    def recur(self,node,remainingsum):
       
        if node is None: 
            return []
        left = self.recur(node.left,remainingsum)
        right = self.recur(node.right,remainingsum)
        tmp=[]
        for x in left:
            tmp.append(node.val+x)
        for x in right:
            tmp.append(node.val+x)
        tmp.append(node.val)
        self.count+=tmp.count(remainingsum)
        return tmp