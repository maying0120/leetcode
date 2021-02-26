from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
 
        def dfs(rank,cur,pre):
            lowrank[cur] = rank
            result =[]
            #print(lowrank)
            for neigh in graph[cur]:
                ### do not include the the incoming path to this vertex since this is the possible ONLY bridge (critical connection) that every vertex needs.

                if neigh == pre: continue
                if not lowrank[neigh]: 
                    result+=dfs(rank+1,neigh,cur)
                    
                lowrank[cur]=min(lowrank[cur],lowrank[neigh])
   # ####### if all the neighbors lowest rank is higher than mine + 1, then it means I am one connecting critical connection ###
                           
                if lowrank[neigh] >= rank+1:
                    result.append([cur,neigh])
           
            return result
            
        graph = collections.defaultdict(list)
        lowrank =  [0]*n
        
        for line in connections:
            graph[line[0]].append(line[1])
            graph[line[1]].append(line[0])
        return dfs(1,0,-1)
        
            