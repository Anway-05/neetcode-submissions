class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        lookup={}
        for ch in s1:
            if ch not in lookup:
                lookup[ch]=1
            else:
                lookup[ch]+=1
        lookup2={}
        i,j=0,0
        while j<len(s1):
            if s2[j] not in lookup2:
                lookup2[s2[j]]=1
            else:
                lookup2[s2[j]]+=1
            j+=1
            if lookup==lookup2:
                return True
        while j<len(s2):
            if s2[j] not in lookup2:
                lookup2[s2[j]]=1
            else:
                lookup2[s2[j]]+=1
            lookup2[s2[i]]-=1
            if lookup2[s2[i]]==0:
                del lookup2[s2[i]]
            j+=1
            i+=1
            if lookup==lookup2:
                return True
        return False
            