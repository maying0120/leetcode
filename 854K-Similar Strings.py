class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        @lru_cache(maxsize=None)
        def helper(A,B):
            if not A and not B:return 0
            if A[0] == B[0]:return helper(A[1:], B[1:])

            res = []
            for i, c in enumerate(B):
                if c == A[0]:
                    res.append(1 + helper(A[1:], B[1:i]+B[0]+B[i+1:]))
            return min(res)
        return helper(A,B)
    
        # dp = {}
        # def helper(A,B):
        #     if A in dp: return dp[A]
        #     if not A or not B or A==B: return 0
        #     if A[0]==B[0]: 
        #         res = helper(A[1:],B[1:])
        #     else:
        #         res = sys.maxsize
        #         for i in range(len(A)):
        #             if A[i]==B[0]: res = min(res,1+helper(A[i]+A[1:i]+A[0]+A[i+1:],B))
        #     dp[A] = res
        #     return res
        # return helper(A,B)