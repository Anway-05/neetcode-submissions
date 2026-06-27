class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        minimum=float('inf')
        if nums[l]<nums[r] or len(nums)==1:
            return nums[l]
        else:
            while l<=r:
                m=(l+r)//2
                if nums[m]<=nums[r]:
                    if nums[m]<minimum:
                        minimum=nums[m]
                    r=m-1
                else:
                    l=m+1
            return minimum