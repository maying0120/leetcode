class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo=[]
        @lru_cache
        def cansplit(word):
            
            if word in wordDict:
                return True
            if word in memo: 
                return False
            else: 
                memo.append(word)
              
            for i in range(len(word)):
                pre = word[:i]
                suf = word[i:]
               # print('pre',pre)
               # print('suf',suf)
                if pre in wordDict and suf in wordDict:
                    return True
                
                if pre in wordDict and cansplit(suf):
                    return True
                    
                if suf in wordDict and cansplit(pre):
                    return True
            return False
        
        return cansplit(s)