class Solution:
    def uniquePaths(self, m: int, n: int):

        memo={}
        def pathWays(r,c):
            if r==m or c==n: return 0
            if r==m-1 and c==n-1:return 1 
            if (r,c) in memo: return memo[(r,c)]


            right=pathWays(r,c+1)
            down=pathWays(r+1,c)
            memo[(r,c)]=right+down
            return right+down

        return pathWays(0,0)

        