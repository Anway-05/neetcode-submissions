class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stored=[]
        for x in strs:
            flag=0
            if not stored:
                stored.append([x])
                flag=1
            else:
                for i,y in enumerate(stored):
                    if sorted(x)==sorted(y[0]):
                        stored[i].append(x)
                        flag=1
            if flag==0:
                stored.append([x])
        return stored
                    
