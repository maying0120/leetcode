# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N)
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        def treerec(node,prval):
            if not node:
                return 
            if node.val in to_delete:
                node.left= treerec(node.left,None)
                node.right= treerec(node.right,None)
                return 
            else:
                if not prval:
                    ans.append(node)
                node.left= treerec(node.left,node.val)
                node.right= treerec(node.right,node.val)
                return node
        
        ans=[]
        treerec(root,None)
        return ans
                
            