class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup={}
        stored=[]
        num=0
        for x in strs:
            freq=[0]*26
            for c in x:
                freq[ord(c)-97]+=1
            key=tuple(freq)
            if key not in lookup:
                lookup[key]=num
                num+=1
                stored.append([])
            stored[lookup[key]].append(x)
        return stored
            