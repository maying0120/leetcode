#bfs
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        if n==0 :
            return 0
        
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit =[0 for _ in range(n)]
        
        q= deque()
        q.append(0)
        count=1
        while 0 in visit:
            while q:
                cur = q.pop()
                visit[cur]=1
                for neigh in graph[cur]:
                    if not visit[neigh]:
                        visit[neigh] = 1
                        q.append(neigh)
            if 0 in visit:
                q.append(visit.index(0))   
                count+=1
        return count

#dfs
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)       
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visit =[0 for _ in range(n)]    
        count=0
        
        def dfs(node):
            
            if not visit[node]: 
                visit[node]=1
                for neig in graph[node]: 
                    dfs(neig)
            return 1

        
        for i in range(n):
            if not visit[i]:
                count+=dfs(i)
                
        return count

#优化版                    
#   def countComponents(n, edges):
# 	g, cnt, seen = collections.defaultdict(set), 0, set()
# 	for u, v in edges: 
# 		g[u].add(v), g[v].add(u)

# 	def dfs(node):
# 		if node not in seen:
# 			seen.add(node)
# 			for nei in g[node]: dfs(nei)
# 		return 1

# 	def bfs(q):
# 		for node in q:
# 			if node not in seen:
# 				q += g[node]
# 				seen.add(node)
# 		return 1

# 	# return sum(dfs(i) for i in range(n) if i not in seen)
# 	return sum(bfs([i]) for i in range(n) if i not in seen)          
            
            