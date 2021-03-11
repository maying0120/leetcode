class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        def bfs(i,j,current_isl):
            
            q =deque()
            q.append((i,j))
            direc = [(1,0),(-1,0),(0,1),(0,-1)]
            current_isl.add((ori_i-i,ori_j-j))
            while q: 
                newi,newj = q.popleft()         
                for d in direc:
                    r = newi+d[0]
                    c = newj+d[1]
                    if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]==1:
                        grid[r][c]=0
                        current_isl.add((r-ori_i,c-ori_j))
                        q.append((r,c))     
        
        
#         def dfs(i,j,current_isl):
#             if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or not grid[i][j] or (i,j) in seen:
#                 return 
#             seen.add((i,j))
#             current_isl.add((i-ori_i,j-ori_j))
#             dfs(i+1,j,current_isl)
#             dfs(i-1,j,current_isl)
#             dfs(i,j+1,current_isl)
#             dfs(i,j-1,current_isl)

    
        seen=set()
        final_isl = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    current_isl = set()
                    ori_i =i
                    ori_j =j
                    bfs(i,j,current_isl)
                    #确保current_isl不为空再添加
                    if current_isl: 
                        final_isl.add(frozenset(current_isl))
                    #print(final_isl)
        return len(final_isl)
                    