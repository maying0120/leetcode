
#Approach 1: Recursion,time complexity O(N)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if root==None:
            return depth
        else:
            left_height= self.maxDepth(root.left)
            right_height= self.maxDepth(root.right)
            return max(left_height,right_height)+1
            
            
#Approach 2:  Iteration,time complexity O(N)
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        stack = []
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        
        return depth