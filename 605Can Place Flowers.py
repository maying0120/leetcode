class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count= 0 
        if len(flowerbed)==1 and flowerbed[0]==0:
            return 1>=n
        
        if len(flowerbed)==2 and flowerbed[0]==0 and flowerbed[1]==0:
            return 1>=n
 
        
        for i in range(1,len(flowerbed)-1,1):

            if i==1 and flowerbed[i-1]==0 and flowerbed[i]==0:
                flowerbed[i-1]=1
                count+=1
            if i==len(flowerbed)-2 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i+1]=1
                count+=1
            if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                count+=1
        print(flowerbed)  
        print(count) 
        return count>=n


# 简化

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        flowerbed = [0] + flowerbed + [0]  # if flowerbed = [0] and n = 1 -> [0,0,0] -> [0,1,0]
        
        if n == 0 :
            return True
        
        for  i in range(1,len(flowerbed)-1) :
            
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0 :
                
                flowerbed[i] = 1
                n -= 1
                
            if n == 0 :
                return True