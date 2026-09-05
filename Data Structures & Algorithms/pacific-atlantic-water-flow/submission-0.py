class Solution:
    def pacificAtlantic(self, heights: List[List[int]]):
        #dfs that returns which lake the water flows 
        # go through all possiblities

        def dfs(r,c,visited):
            visited.add((r,c))
            t=[False,False]

            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                rnew=r+dr
                cnew=c+dc
                if  cnew<0 or rnew<0: 
                    t[0]=t[0] or True
                    t[1]=t[1] or False
                    continue
                if cnew>=len(heights[0]) or rnew>=len(heights):
                    t[0]=t[0] or False
                    t[1]=t[1] or True
                    continue
                if (rnew,cnew) not in visited and ( heights[rnew][cnew]<=heights[r][c] ):
                    temp=dfs(rnew,cnew,visited)
                    t[0]=t[0] or temp[0]
                    t[1]=t[1] or temp[1]
            return t

        final=[]
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if dfs(i,j,set())[0] and dfs(i,j,set())[1]: final.append([i,j])
        return final


        