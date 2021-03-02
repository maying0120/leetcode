class Solution:        
    # time：O(log(n!))  
    # space:O(1)
    def binarysearch(self,matrix,target,s,v):
        
        lo =s
        hi = len(matrix[0])-1 if v else len(matrix)-1
        
        while lo<=hi:
            
            mid = lo+(hi-lo)//2
            if v:
                print('matrix[s][mid]',matrix[s][mid])
                if matrix[s][mid] > target:
                    hi = mid-1
                elif matrix[s][mid] <target:
                    lo =mid+1
                else:
                    return True
            else:
                print('matrix[mid][s]',matrix[mid][s])
                print('s',s)
                if matrix[mid][s] > target:
                    hi = mid-1
                elif matrix[mid][s] <target:
                    lo =mid+1
                else:
                    return True
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:     
        if not matrix: return False
        
        for i in range(min(len(matrix),len(matrix[0]))):
            res1 = self.binarysearch(matrix,target,i,True)
            res2 = self.binarysearch(matrix,target,i,False)
            if res1 or res2:
                return True
        return False
            
        
        
        
        
        # visit = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        # def dfs(matrix,i,j,target):
        #     if i<0 or j<0 or i>len(matrix)-1 or j>len(matrix[0])-1:
        #         return False  
        #     if visit[i][j]==1:
        #         return False
        #     visit[i][j]=1
        #     if matrix[i][j]==target:
        #         return True    
        #     if matrix[i][j]<target:
        #         if  dfs(matrix,i+1,j,target):
        #             return True
        #         if dfs(matrix,i,j+1,target):
        #             return True 
        #     return False    
        # return dfs(matrix,0,0,target)
