# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Iterations
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        if not root:
            return ans
        stack=[]
        order=[]
        stack.append(root)
        while stack:
            node = stack.pop()
            order.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return order
    
 #   Recursive
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []

        
