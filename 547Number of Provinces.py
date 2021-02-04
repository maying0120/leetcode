class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = [0] *len(isConnected)
        
        count=0
        for i in range(len(isConnected)):
            if self.visited[i]==0:
                self.dfs(i,isConnected,self.visited)
                count+=1
        return count
                
        
    
    
    def dfs(self,i,isConnected,visited):
        
        for j in range(len(isConnected)):
            if isConnected[i][j]==1 and self.visited[j]==0:
                self.visited[j]=1
                #继续搜索i的朋友
                self.dfs(j,isConnected,visited)
    
        