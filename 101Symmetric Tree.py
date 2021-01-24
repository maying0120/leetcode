# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        else:
            return self.panduan(root.left,root.right)
    
    def panduan(self,left,right):

        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        
        if left.val== right.val:
            outl = self.panduan(left.left,right.right)
            inl = self.panduan(left.right,right.left)
            return outl and inl
            
        else:
            return False