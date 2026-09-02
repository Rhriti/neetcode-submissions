from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) :
        g=defaultdict(list)
        for ele in prerequisites:g[ele[1]].append(ele[0])

        visit=set()
        def cycle(node,path):
            if node in path: return True
            if node in visit: return False
            visit.add(node)
            path.add(node)
            temp=False
            for ch in g[node]: temp = temp or cycle(ch,path)
            path.remove(node)
            return temp

        for node in range(numCourses):
            if node not in visit: 
                if cycle(node,set()):return False
        return True

        