class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0 
        r = len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                
                temp1= s[:l]+s[l+1:]
                temp2 = s[:r]+s[r+1:]
                return temp1==temp1[::-1] or temp2==temp2[::-1]
        #"aba->ture"
        return True