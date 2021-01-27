class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g = sorted(g)
        s = sorted(s)
        
        children = 0
        cookie = 0
        while cookie < len(s) and children < len(g):
            if s[cookie]>=g[children]:
                children+=1
            
            cookie+=1
        return children