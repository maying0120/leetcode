
#将是否是子树问问题->是否相等的问题
#判断两个树相等三个条件 && 1:当前两个树的根结点值相等；并且s的左子树和t的左子树相等；s的右边子树和t的右子树相等
#判断t是否为s子树的三个条件 or 1:当前两棵树相等； 2:或者，t是s的左子树 3:或者，t是s的右子树





class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return str(t) in str(s)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        elif not s or not t:
            return False
        return self.isSame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    
    def isSame(self,s,t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        return s.val==t.val and self.isSame(s.left,t.left) and self.isSame(s.right,t.right)