class Solution:
    def rob(self, nums: List[int]):

        pmax=0
        ppmax=0
        for i in range(len(nums)):
            currmax=max(nums[i]+ppmax,pmax)
            temp=pmax
            pmax=currmax
            ppmax=temp
        return currmax
        