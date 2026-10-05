#we need to avoid duplicates
from collections import defaultdict 
class Solution:
    def twoSum(self, nums: List[int], target: int):
        g=defaultdict(list)
        for i in range(len(nums)):g[nums[i]].append(i)
        
        for j in range(len(nums)):
            find=target-nums[j]
            if nums[j]==find:
                if len(g[find])>1:
                    return [g[find][0],g[find][1]]
            else:
                if find in g:return [j,g[find][0]]
            
        

        
        