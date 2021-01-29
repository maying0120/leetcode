class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
                
        n = len(s)
        if n*k==0:
            return 0
        
        hashmap = defaultdict()
        left,right, res =0,0,1
        while right<n:
            hashmap[s[right]]  = right
            right+=1
            
            if len(hashmap)==k+1:
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                left = del_idx +1
            res = max(res,right-left)
        return res
            
                    