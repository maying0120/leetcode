import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c==0:
            return True
        
        end = int(math.sqrt(c))
        for i in range(0,end+1):
            temp = math.sqrt(c -i*i)
            if int(temp)==temp:
                return True
        return False
            