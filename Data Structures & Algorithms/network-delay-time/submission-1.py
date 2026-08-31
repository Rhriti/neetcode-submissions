from collections import defaultdict
import heapq as hq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int):
        g=defaultdict(dict)
        for ele in times:g[ele[0]][ele[1]]=ele[2]

        stack=[(0,k)]  #(cost,node)
        visited=set()
        mintime=0
        while stack:
            out=hq.heappop(stack)
            out_node=out[1]
            out_cost=out[0]
            if out_node in visited: continue

            mintime=max(mintime,out_cost)
            visited.add(out_node)

            if len(visited)==n:return mintime
        
            
            
            for ch in g[out_node]:
                if ch not in visited:
                    hq.heappush(stack,(out_cost+g[out_node][ch],ch))
        return -1
                




        