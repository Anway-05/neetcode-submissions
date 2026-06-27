class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_1,right_1=0,len(matrix)-1
        while left_1<=right_1:
            mid_1=(left_1+right_1)//2
            if matrix[mid_1][0]<=target and matrix[mid_1][-1]>=target:
                left,right=0,len(matrix[mid_1])-1
                while left<=right:
                    mid=(right+left)//2
                    if matrix[mid_1][mid]==target:
                        return True
                    if matrix[mid_1][mid]>target:
                        right=mid-1
                    elif matrix[mid_1][mid]<target:
                        left=mid+1
                return False

            if matrix[mid_1][0]>target:
                right_1=mid_1-1

            elif matrix[mid_1][-1]<target:
                left_1=mid_1+1
                
        return False


