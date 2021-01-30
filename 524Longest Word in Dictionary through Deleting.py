class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        
        longw=''
        for w in d:
            p1=0
            p2=0
            while p1<len(w) and p2<len(s):
                if w[p1]==s[p2]:
                    p1+=1
                    p2+=1
                else:
                    p2+=1
            #这个==len(w) 因为最后一个字符相等之后还+1   
            if p1==len(w):
                if len(w)>len(longw):
                    longw = w
                 # Hint: 'ac' is smaller than 'ba'
                elif len(w)==len(longw):
                    longw = min(w,longw)
        
        return longw
            