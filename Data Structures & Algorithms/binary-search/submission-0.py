class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[left]==target:
                return left
            if nums[right]==target:
                return right
            if nums[mid]==target:
                return mid
            if target<nums[mid]:
                left,right=left, mid-1
            elif target>nums[mid]:
                left,right=mid+1,right
        return -1