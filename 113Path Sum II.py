# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        pathsList=[]
        self.retree(root,targetSum,[],pathsList)
        return pathsList
        
        
        
    def  retree(self,node,remainingSum,pathNodes, pathsList):
       
        if node is None: return 
        pathNodes.append(node.val)
        if node.left is None and node.right is None and node.val == remainingSum:
           # print(pathNodes)
            pathsList.append(list(pathNodes))
        else:
            
            self.retree(node.left,remainingSum-node.val,pathNodes,pathsList)
            self.retree(node.right,remainingSum-node.val,pathNodes,pathsList)
        pathNodes.pop()
        