class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        dic={}
        dic[keysPressed[0]]=releaseTimes[0]
        for i in range(1,len(keysPressed)):
            if keysPressed[i] not in dic:
                dic[keysPressed[i]]=releaseTimes[i]-releaseTimes[i-1]
            else:
                if releaseTimes[i]-releaseTimes[i-1]>dic[keysPressed[i]]:
                    dic[keysPressed[i]]=releaseTimes[i]-releaseTimes[i-1]
        
        maxtime = 0
        key='a'
        print(dic)
        for k,v in dic.items():
            if v>maxtime:
                if key!=k:
                    maxtime = v
                    key = k
                else:
                    if key<k:
                        key=k
        return key
        