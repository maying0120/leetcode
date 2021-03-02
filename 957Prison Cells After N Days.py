class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen =[]
      
        idx=0
        precell = cells
        while idx<n:
            newcell=[0]*len(cells)
            for i in range(1,len(precell)-1): 
                if precell[i-1]==precell[i+1]:
                    newcell[i]=1
              
            if newcell not in seen:
                seen.append(newcell)
            else:
                print('break',newcell)
                break
            precell = newcell
            idx+=1
        if idx==n:
            return seen[-1]
        print(seen)
        
        remind = n%(len(seen))
        print(remind)
        return seen[remind-1]
            