class Solution:
    def __init__(self):
        self.find  = False
    
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board)==0 or len(board[0])==0:
            return False
        m ,n = len(board),len(board[0])
        visited = [[False]*len(board[0]) for i in range(len(board))]
        print(visited)
        
       #find = False
        for i in range(m):
            for j in range(n):
                
                self.dfs(board,visited,i,j,0,self.find,word)
                if self.find==True:
                    return True
        return False
             
    
    def dfs( self,board,visited,i,j,pos,find,word):
        # 
        if  self.find==True:
            return 
     
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
            return 
          
        if visited[i][j]: 
            return 
        
        if board[i][j]!=word[pos] or  self.find:
            return
        
        if(pos==(len(word)-1)):
            self.find = True
         
            return True
        
        visited[i][j] = True        
        self.dfs(board,visited,i+1,j,pos+1,find,word)
        self.dfs(board,visited,i-1,j,pos+1,find,word)
        self.dfs(board,visited,i,j+1,pos+1,find,word)
        self.dfs(board,visited,i,j-1,pos+1,find,word)  
        
        visited[i][j] = False
            