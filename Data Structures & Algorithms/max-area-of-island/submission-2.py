class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]):
        
        def dfs(r,c):
            #base conditions
            if (r,c) in covered1 or r>=len(grid) or r<0 or c>=len(grid[0]) or c<0 or  grid[r][c]==0: return 0

            covered1.add((r,c))
            return dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)+1

        
        covered1=set()
        maxarea=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0 or (i,j) in covered1:continue
                area=dfs(i,j)
                maxarea=max(maxarea,area)
        return maxarea

