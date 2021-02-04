class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        res=[]
        self.dire = [(1,0),(-1,0),(0,1),(0,-1)]
        res=[]
        m= len(matrix)
        n = len(matrix[0])
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        

        for i in range(m):
            self.dfs(matrix,m,n,p_visited,i,0)
            self.dfs(matrix,m,n,a_visited,i,n-1)
        
        for j in range(n):
            self.dfs(matrix,m,n,p_visited,0,j)
            self.dfs(matrix,m,n,a_visited,m-1,j)
            
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i,j])
        return res
                    
            
    
    
    
    
    
    def dfs(self,matrix,m,n,visited,i,j):
        visited[i][j] = True
        
        for d in self.dire:
            x = i+d[0]
            y = j+d[1]
            if x< 0 or x>=m or y<0 or y>=n or visited[x][y] or matrix[x][y]<matrix[i][j]:
                continue
            self.dfs(matrix,m,n,visited,x,y)
        
        
        
        
        
    
        