
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,prev,word,board):
    
            
            if not 0<= i < len(board) or not 0 <= j < len(board[0]):
                #print('h2')
                return False
            cur = prev+ board[i][j]   
           
            if cur == word:
                return True
            if not word.startswith(cur):
                #print('h3')
                return False
            temp = board[i][j]
            # avoid visit agian
            board[i][j]="#"
            
            steps=[[0,-1],[-1,0],[0,1],[1,0]]
            for ci,cj in steps:
                if dfs(ci+i,cj+j,cur,word,board):
                    return True
            board[i][j]=temp
            return False
              
        if not board and word: return False
        if not word and board: return True
      
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,'',word,board):
                    return True
        return False





class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,prev,word,board,visit):
    
            if (i,j) in visit:
                #print('h1')
                return False
            
            if not 0<= i < len(board) or not 0 <= j < len(board[0]):
                #print('h2')
                return False
            cur = prev+ board[i][j]   
           #print('cur',cur)
            if cur == word:
                return True
            if not word.startswith(cur):
                #print('h3')
                return False
            nxt_visit = visit | {(i, j)}
            #print(visit)
            #visit.add((i,j))
            
            steps=[[0,-1],[-1,0],[0,1],[1,0]]
            for ci,cj in steps:
                if dfs(ci+i,cj+j,cur,word,board,nxt_visit):
                    return True
            return False
              
        if not board and word: return False
        if not word and board: return True
      
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,'',word,board,set()):
                    return True
        return False