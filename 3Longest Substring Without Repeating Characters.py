class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        left =0 
        ans = 0
        mp={}
        n = len(s)
        for j in range(n):
            if s[j] in mp:
                left = max(mp[s[j]],left)
    #将每个character最新出现的index更新到mp中，然后
            ans = max(ans,j-left+1)
            mp[s[j]]= j+1
        return ans