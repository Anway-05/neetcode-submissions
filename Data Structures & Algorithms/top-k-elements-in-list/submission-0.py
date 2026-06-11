class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup={}
        for x in nums:
            if x not in lookup:
                lookup[x]=1
            else:
                lookup[x]+=1
        stored=[]
        for i in range(k):
            key=max(lookup,key=lookup.get)
            stored.append(key)
            lookup.pop(key)
        return stored