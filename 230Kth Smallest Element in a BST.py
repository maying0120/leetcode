# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
             
        def inorder(node,res):
            
            if node.left is not None:
                inorder(node.left,res)         
            if node:
                res.append(node.val)            
            if node.right is not None:
                inorder(node.right,res)        
            return res
        
        arr=[]
        inorder(root,arr)
        return arr[k-1]
                