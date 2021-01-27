#Algorithm
#Now the algorithm is straightforward :
#Sort the balloons by end coordinate x_end.
#Initiate the end coordinate of a balloon which ends first : first_end = points[0][1].
#Initiate number of arrows: arrows = 1.
#Iterate over all balloons:
#If the balloon starts after first_end:
#Increase the number of arrows by one.
#Set first_end to be equal to the end of the current balloon.
#Return arrows.

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key= lambda x:x[1])
        if not points:
            return 0
        
        arrow= 1 
        first_end = points[0][1]
        for i in range(len(points)):
            if points[i][0]> first_end:
                arrow+=1
                first_end =points[i][1]
        return arrow
                