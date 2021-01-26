# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        self.d = 0
        self.ans = 0 
        
        def left_tree(node,depth):
            if node is None:
                return 0
            left_tree(node.left,depth+1)           
            if depth > self.d:
                self.d = depth
                self.ans = node.val
            left_tree(node.right,depth+1)
            
        left_tree(root,1)
        return self.ans
                