class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_m,column_m=len(matrix),len(matrix[0])
        l,r=0,(row_m*column_m-1)
        while l<=r:
            m=(l+r)//2
            row,col=m//column_m,m%column_m
            if matrix[row][col]>target:
                r=m-1
            elif matrix[row][col]<target:
                l=m+1
            else:
                return True
        return False