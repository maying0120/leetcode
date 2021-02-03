# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.map={}
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root in self.map:
            return self.map[root]
        total = 0
        if root.left:
            total += self.rob(root.left.right) + self.rob(root.left.left)
        
        if root.right:
            total += self.rob(root.right.right) + self.rob(root.right.left)
        
        self.map[root] = max(root.val+total, self.rob(root.left) +self.rob(root.right))
        return self.map[root]