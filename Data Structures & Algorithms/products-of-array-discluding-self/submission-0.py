class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        count=0
        indices=[]
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
                indices.append(i)
            else:
                product*=nums[i]
        for i in range(len(nums)):
            if count==0:
                nums[i]=int(product/nums[i])
            elif count>=2:
                nums[i]=0
            else:
                if i==indices[0]:
                    nums[i]=product
                else:
                    nums[i]=0
        return nums
