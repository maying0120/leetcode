import itertools
from collections import defaultdict

class Solution0:
    def diffWaysToCompute(self, input):  # Divide and conquer
        
        def _ways(string):
            res = []
            if not string:
                return res
            
            for i, c in enumerate(string):
                if c in "+-*":
                    left = _ways(string[0:i])
                    right = _ways(string[i + 1:])

                    for l in left:  # 两个for循环可以用 itertools.product 优化
                        for r in right:
                            if c == '+':  # 操作符可以用lambda 优化
                                res.append(l + r)
                            elif c == '-':
                                res.append(l - r)
                            elif c == '*':
                                res.append(l * r)
            if not res:   # 说明没有operator，直接返回结果
                res.append(int(string))
            return res

        return _ways(input)


class Solution1:
    def diffWaysToCompute(self, input):
        """
        Divide and conquer => lambda and itertools.product
        :type input: str
        :rtype: List[int]
        """
        ops = {'+': lambda a,b: a+b,
               '-': lambda a, b: a-b,
               '*': lambda a, b: a*b}

        def _ways(string):
            res = []
            if not string:
                return res

            for i, c in enumerate(string):
                if c in "+-*":
                    left = _ways(string[0:i])
                    right = _ways(string[i + 1:])
                    res += [ops[c](l, r) for l, r in itertools.product(left, right)]
            if not res:
                res.append(int(string))
            return res

        return _ways(input)


class Solution2:
    def diffWaysToCompute(self, input):
        """
        Memoization.
        :type input: str
        :rtype: List[int]
        """
        ops = {'+': lambda a,b: a+b,
               '-': lambda a, b: a-b,
               '*': lambda a, b: a*b}
        cache = defaultdict(str)  # 全局初始化cache

        def _ways(string):
            if cache[string]:  # 先检查cache
                return cache[string]
            res = []
            if not string:
                return res

            for i, c in enumerate(string):
                if c in "+-*":
                    left = _ways(string[0:i])
                    right = _ways(string[i + 1:])
                    res += [ops[c](l, r) for l, r in itertools.product(left, right)]
            if not res:
                res.append(int(string))
            cache[string] = res  # 返回结果前记得保存cache
            return res

        return _ways(input)