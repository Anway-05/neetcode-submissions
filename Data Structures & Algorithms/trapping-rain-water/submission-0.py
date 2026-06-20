class Solution:
    def trap(self, height: List[int]) -> int:
        max_left=[]
        max_right=[]
        left_max,right_max=0,0
        i=0
        while i<len(height):
            max_left.append(left_max)
            if height[i]>left_max:
                left_max=height[i]
            max_right.append(right_max)
            if height[len(height)-i-1]>right_max:
                right_max=height[len(height)-i-1]
            i+=1
        max_right.reverse()
        i=0
        water_area=0
        while i<len(height):
            water_area+=max((min(max_left[i],max_right[i])-height[i]),0)
            i+=1
        return water_area
