class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        vistied=[]
        ins = instructions+instructions+instructions+instructions     
        vistied.append([0,0])
        ori=[1,2,3,4]
        flag=1
        for i in ins:
            if i=='G':
                last=vistied[-1]
                if flag==1:
                    vistied.append([last[0]+1,last[1]+1])
                elif flag==2:
                    vistied.append([last[0]-1,last[1]])
                
                elif flag==3:
                     vistied.append([last[0]-1,last[1]-1])         
                elif flag==4:
                     vistied.append([last[0]+1,last[1]])               
            elif i=='R': 
                temp = ori.index(flag)
                if temp+1<=3:
                    flag = ori[temp+1]
                else:
                    flag=ori[temp+1-4]
                
            elif i=='L':
                temp = ori.index(flag)
                if temp-1>=0:
                    flag = ori[temp-1]
                else:
                    flag = ori[temp-1+4]
            print(vistied)
           
        for j in instructions:
            if j=='G':
                last=vistied[-1]
                if flag==1:
                    if [last[0]+1,last[1]+1] not in vistied:
                        return False
                    else:
                        vistied.append([last[0]+1,last[1]+1])
                elif flag==2:
                    if [last[0]-1,last[1]] not in vistied:
                        return False
                    else:
                        vistied.append([last[0]-1,last[1]] )
                
                elif flag==3:
                    if [last[0]-1,last[1]-1] not in vistied:
                        print([last[0]-1,last[1]-1] )
                        return False
                    else:
                        vistied.append([last[0]-1,last[1]-1])
                        
                elif flag==4:
                    if [last[0]+1,last[1]] not in vistied:
                        return False   
                    else:
                        vistied.append( [last[0]+1,last[1]])
            elif j=='R': 
                temp = ori.index(flag)
                if temp+1<=3:
                    flag = ori[temp+1]
                else:
                    flag=ori[temp+1-4]
                
            elif j=='L':
                temp = ori.index(flag)
                if temp-1>=0:
                    flag = ori[temp-1]
                else:
                    flag = ori[temp-1+4]
        return True

    # We do not need to run 4 cycles to identify the limit cycle trajectory. One cycle is enough. #There could be two situations here.

#First, if the robot returns to the initial point after one cycle, that's the limit cycle trajectory.

#Second, if the robot doesn't face north at the end of the first cycle, that's the limit cycle #trajectory. Once again, that's the consequence of the plane symmetry for the repeated cycles ##[proof].


# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         # north = 0, east = 1, south = 2, west = 3
#         directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#         # Initial position is in the center
#         x = y = 0
#         # facing north
#         idx = 0
        
#         for i in instructions:
#             if i == "L":
#                 idx = (idx + 3) % 4
#             elif i == "R":
#                 idx = (idx + 1) % 4
#             else:
#                 x += directions[idx][0]
#                 y += directions[idx][1]
        
#         # after one cycle:
#         # robot returns into initial position
#         # or robot doesn't face north
#         return (x == 0 and y == 0) or idx != 0      s