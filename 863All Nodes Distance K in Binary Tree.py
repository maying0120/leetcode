#Approach 1: Annotate Parent
#Intuition
#If we know the parent of every node x, we know all nodes that are distance 1 from x. We can then perform a breadth first search from the target node to find the answer.
#Algorithm
#We first do a depth first search where we annotate every node with information about it's parent.
#After, we do a breadth first search to find all nodes a distance K from the target.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        def dfs(node,par=None):
            if node:
                node.par = par
                dfs(node.left,node)
                dfs(node.right,node)
        dfs(root)
        
        q=deque()
        q.append([target,0])
        res=[]
        seen={target}
        
        while q:
            curnode,level = q.popleft()
       
            if level==K:
 
                res.append(curnode.val)
            for nei in (curnode.left,curnode.right,curnode.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    q.append([nei,level+1])
        
        return res
            
        