# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # An empty root is one of the test cases!
        if not root:
            return 0
        def subtree(node,is_left):
            # Base case: This is a leaf node.
            if node.left is None and node.right is None:
                return node.val if is_left else 0
            ans = 0
              # Recursive case: We need to add and return the results of the left and right subtrees.
            if node.left:
                ans +=subtree(node.left,True)
            if node.right:
                ans += subtree(node.right,False)
            return ans
   
        return subtree(root,False)
        