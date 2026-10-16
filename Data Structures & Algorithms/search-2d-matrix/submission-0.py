class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        R=len(matrix)
        C=len(matrix[0])
        i=0
        j=R*C-1
        while i<=j:
            mid=(i+j)//2
            r=mid//C
            c=mid%C
            ele=matrix[r][c]
            if ele==target:return True
            if ele>target:
                j=mid-1
            else: i=mid+1        
        return False