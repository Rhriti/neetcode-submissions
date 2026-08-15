class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]):

        memo={}
        def pathWays(r,c):
            if r==len(grid) or c==len(grid[0]) or grid[r][c]==1 : return 0
            if r==len(grid)-1 and c==len(grid[0])-1:return 1
            if (r,c) in memo: return memo[(r,c)]


            right=pathWays(r,c+1)
            bottom=pathWays(r+1,c)
            memo[(r,c)]=right+bottom
            return right+bottom
        return pathWays(0,0)
        