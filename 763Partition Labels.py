class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        
        # 统计字符最后一次出现的位置
        last = {c: i for i, c in enumerate(S)}
       # print(last)
        start = end = 0
        ans =[]
        #遍历整个字符串
        for i,c in enumerate(S):
            end = max(end,last[c])           
            if i==end:
                ans.append(end-start+1)
                start = end+1
        return ans
            
            
            