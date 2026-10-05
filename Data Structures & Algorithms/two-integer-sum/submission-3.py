#we need to avoid duplicates
from collections import defaultdict 
class Solution:
    def twoSum(self, nums: List[int], target: int):
        prev_hash={}
        for i in range(len(nums)):
            find=target-nums[i]
            if find in prev_hash:
                return [prev_hash[find],i]
            prev_hash[nums[i]]=i

            
        

        
        