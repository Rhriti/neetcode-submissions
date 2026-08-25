from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]):
        q=deque()
        fresh=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:fresh+=1
                if grid[r][c]==2: q.append((r,c))
        
        time=0
        while q and fresh>0:
            dir=[(1,0),(0,1),(-1,0),(0,-1)]
            for _ in range(len(q)):
                out=q.popleft()
                rout=out[0]
                cout=out[1]

                for dr,dc in dir:
                    r=rout+dr
                    c=cout+dc

                    if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]==1:
                        grid[r][c]=2
                        q.append((r,c))
                        fresh-=1
            time+=1

        return time if fresh<=0 else -1



        