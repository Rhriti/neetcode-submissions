class Solution:
    def numIslands(self, grid: List[List[str]]):

        def dfs(r,c):
            #have to traverse all the connected 1s 
            if not grid[r][c]=="1" or (r,c) in covered:return 

            covered.add((r,c))
            if r+1<len(grid):
                dfs(r+1,c)
            if c+1<len(grid[0]):
                dfs(r,c+1)
            if c-1>=0:
                dfs(r,c-1)
            if r-1>=0:
                dfs(r-1,c)

    
        count=0
        covered=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in covered:
                    dfs(i,j)
                    count+=1
        return count
            