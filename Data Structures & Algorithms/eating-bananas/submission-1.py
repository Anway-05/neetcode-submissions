class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        k=max(piles)
        while l<=r:
            time_taken=0
            m=((l+r)//2)
            for x in piles:
                time_taken+=((x+m-1)//m)
            if time_taken<=h and m<k:
                k=m
            if time_taken>h:
                l=m+1
            else:
                r=m-1
        return k
            
