# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return 
        
        rootvale=preorder[0]
        inorderindex = inorder.index(rootvale)
        root = TreeNode(rootvale)
        
        root.left = self.buildTree(preorder[1:inorderindex+1],inorder[:inorderindex])
        root.right = self.buildTree(preorder[inorderindex+1:],inorder[inorderindex+1:])
        return root
        