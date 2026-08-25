class Solution:
    def orangesRotting(self, grid: List[List[int]]):
        stack=[]
        v=set()
        totalfruit=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==2:
                    stack.append((r,c))
                    totalfruit+=1
                    v.add((r,c))
                if grid[r][c]==1:totalfruit+=1
        time=0
        while stack:
            newstack=[]
            for _ in range(len(stack)):
                out=stack.pop()
                rout=out[0]
                cout=out[1]
                if rout+1<len(grid) and (rout+1,cout) not in v and grid[rout+1][cout]==1:
                    v.add((rout+1,cout))
                    newstack.append((rout+1,cout))
                if rout-1>=0 and (rout-1,cout) not in v and grid[rout-1][cout]==1:
                    v.add((rout-1,cout))
                    newstack.append((rout-1,cout))
                if cout+1<len(grid[0]) and (rout,cout+1) not in v and grid[rout][cout+1]==1:
                    v.add((rout,cout+1))
                    newstack.append((rout,cout+1))
                if cout-1>=0 and (rout,cout-1) not in v and grid[rout][cout-1]==1:
                    v.add((rout,cout-1))
                    newstack.append((rout,cout-1))
            stack=newstack
            time+=1
        print("totalfruit",totalfruit)
        print("v",v)
        return max(0,time-1) if len(v)==totalfruit else -1
                



        