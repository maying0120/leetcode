class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        groupc = defaultdict(list)
        
        for i,s in enumerate(strings):
            order=""
            for j in range(1,len(s)):
                tmp = (ord(s[j])-ord(s[j-1]))%26
                #al=['11'] abc=['11']
                if tmp>=10:
                    order+='0'                                   
                order+=str(tmp)
            groupc[order].append(s)
        print('groupc',groupc)
        return list(groupc.values())