class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target>matrix[i][-1]:
                continue
            left,right=0,len(matrix[i])-1
            while left<=right:
                mid=(right+left)//2
                if matrix[i][mid]==target:
                    return True
                if matrix[i][mid]>target:
                    right=mid-1
                elif matrix[i][mid]<target:
                    left=mid+1
        return False

