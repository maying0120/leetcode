class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxcount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    maxcount = max(maxcount,self.dfs(grid,i,j))
        return maxcount        
        
    
    
    def dfs(self,grid,r,c):
        if r<0 or r>=len(grid) or c <0 or c>=len(grid[0]):
            return 0
        if grid[r][c]==0:
            return 0
        # mark as visited
        grid[r][c]=0
        return 1+self.dfs(grid,r-1,c)+self.dfs(grid,r,c-1)+self.dfs(grid,r+1,c)+self.dfs(grid,r,c+1)


class Solution:
    
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, self.m, self.n = 0, len(grid), len(grid[0])
        visited = set()
        for i in range(self.m):
            for j in range(self.n):
                if (i, j) not in visited and grid[i][j]:
                    self.count = 1
                    visited.add((i, j))
                    self.dfs(i, j, grid, visited)
                    ans = max(self.count, ans)

        return ans
    
    def dfs(self, i, j, grid, visited):
        for dx, dy in self.DIRECTIONS:
            x, y = i + dx, j + dy
            if (0 <= x < self.m and 0 <= y < self.n and
                (x, y) not in visited and grid[x][y]):
                self.count += 1
                visited.add((x, y))
                self.dfs(x, y, grid, visited)
