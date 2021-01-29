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
            
#java
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        
        int n= s.length();
        if (n*k==0)
        {
            return 0;
        }
        int left=0;
        int right =0;
        Map<Character,Integer> map = new HashMap<>();
        
        int res=1;
        while(right<n)
        {
            map.put(s.charAt(right),right);
            right++;
            
            if (map.size()==k+1)
            {
                int lowidx = Collections.min(map.values());
                map.remove(s.charAt(lowidx));
                left = lowidx+1;
                
            }
            res = Math.max(res,right-left);
            
        }
        return res;
        
    }
}
