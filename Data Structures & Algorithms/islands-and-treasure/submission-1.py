from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]):
        queue=deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0: queue.append([r,c,0])
        visited=set()
        while queue:
            out=queue.popleft()
            r,c=out[0],out[1]
            cost=out[2]
            #base
            if r>len(grid)-1 or r<0 or c>len(grid[0])-1 or c<0 or grid[r][c]==-1 or (r,c) in visited :continue

            visited.add((r,c))
            grid[r][c]=cost
            queue.append([r+1,c,cost+1])
            queue.append([r-1,c,cost+1])
            queue.append([r,c+1,cost+1])
            queue.append([r,c-1,cost+1])

        
            

        