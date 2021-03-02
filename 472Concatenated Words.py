class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
  # add memo 
        d = set(words)
        memo={}
   
        
        def dfs(word):
            if word in memo:
                return memo[word]
            for i in range(1,len(word)):
                pre = word[:i]
                suf = word[i:]
        
                
                if pre in d and suf in d:
                    memo[word] = True
                    return True
                elif pre in d and dfs(suf):
                    memo[word] = True
                    return True
                elif suf in d and dfs(pre):
                    memo[word] = True
                    return True
            memo[word] = False
            return False
        
        res=[]
        for w in words:
            if dfs(w):
                res.append(w)
        return res

        
        
        
# TlE        
#         d = set(words)
   
        
#         def dfs(word):
#             for i in range(1,len(word)):
#                 pre = word[:i]
#                 suf = word[i:]
        
                
#                 if pre in d and suf in d:
#                     return True
#                 elif pre in d and dfs(suf):
#                     return True
#                 elif suf in d and dfs(pre):
#                     return True
#             return False
        
#         res=[]
#         for w in words:
#             if dfs(w):
#                 res.append(w)
#         return res
        