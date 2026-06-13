class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        stored1=[1]*len(nums)
        stored2=[1]*len(nums)
        i=1
        while i<len(nums):
            stored1[i]=nums[i-1]*stored1[i-1]
            stored2[len(nums)-i-1]=stored2[len(nums)-i]*nums[len(nums)-i]
            i+=1
        for i in range(len(nums)):
            nums[i]=stored1[i]*stored2[i]
        return nums
