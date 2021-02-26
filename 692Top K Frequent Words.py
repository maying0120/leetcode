class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count={}
        for w in words:
            if w not in count:
                count[w]=1
            else:
                count[w]+=1
                
        new = sorted(count.items(),key=lambda x:(-x[1],x[0]))
        #排序之后由dict变成list，所以无法用keys等关键字
        res=[]
        for i in range(k):
            res.append(new[i][0])
        return res
        
        
      #  counter = collections.Counter(words)
      #  top_k = heapq.nsmallest(k, counter.items(), key=lambda x: (-x[1], x[0])) 
      #  return [word[0] for word in top_k]
    