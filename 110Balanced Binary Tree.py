# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        a,b= self.treenum(root)
        return b
        
    def treenum(self,node):
        if node is None:
            return (0,True)
       
        left_height,is_l_bal = self.treenum(node.left)
        right_height,is_r_bal = self.treenum(node.right)
        
        if is_l_bal and is_r_bal and abs(left_height-right_height)<=1:
            return (1+max(left_height,right_height),True)
                
        return (1+max(left_height,right_height),False)
        