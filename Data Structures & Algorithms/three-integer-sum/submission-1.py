class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stored=[]
        k=0
        while k<len(nums)-1:
            i,j=k+1,len(nums)-1
            while i<j:
                if nums[i]+nums[j]+nums[k] == 0:
                    stored.append([nums[k],nums[i],nums[j]])
                    i+=1
                    j-=1
                    while i<j and nums[i-1]==nums[i]:
                        i+=1
                    while i<j and nums[j+1]==nums[j]:
                        j-=1
                elif nums[i]+nums[j]+nums[k]>0:
                    j-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    i+=1
            k+=1
            while k<len(nums)-2 and nums[k-1]==nums[k]:
                k+=1
        return stored