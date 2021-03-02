class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[]
        
        s.append(asteroids[0])
        
        for i in range(1,len(asteroids)):
            #only collosions when top of the stack >0 and new <0
            while s and asteroids[i]<0<s[-1]:
                if s[-1] < abs(asteroids[i]):
                    s.pop()
                    continue
                elif s[-1]==abs(asteroids[i]):
                    s.pop()
                #when run the if loop need break while loop 
                break
            #when not run the while loop just add new node
            else:
                s.append(asteroids[i])
                    
            
            
        return s
                        
# Time Complexity: O(N), where N is the number of asteroids. Our stack pushes and pops each asteroid at most once.

#Space Complexity: O(N). We use a stack to keep track of the intermediate results. In the worst case, the states do not evolve at the end, i.e. we need O(N) space where NN is the number of input asteroids.    

# Algorithm

# Say we have our answer as a stack with rightmost asteroid top, and a new asteroid comes in. If new is moving right (new > 0), or if top is moving left (top < 0), no collision occurs.

# Otherwise, if abs(new) < abs(top), then the new asteroid will blow up; if abs(new) == abs(top) then both asteroids will blow up; and if abs(new) > abs(top), then the top asteroid will blow up (and possibly more asteroids will, so we should continue checking.)