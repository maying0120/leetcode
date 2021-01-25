class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        # for a given node - swap left and right nodes
        # repeat the same for all child nodes
        # edge cases ..
        #   left node or right node is empty/None
        #   given node is empty/None
        
        if (root is not None):
            # swap child nodes
            tmp = root.left
            root.left = root.right
            root.right = tmp
            # invert children
            self.invertTree(root.left)
            self.invertTree(root.right)
        
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#  写到一行可以，写到两行不行
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return     
        root.left,root.right= self.invertTree(root.right),self.invertTree(root.left)
        #root.right = self.invertTree(root.left)
        return root
            