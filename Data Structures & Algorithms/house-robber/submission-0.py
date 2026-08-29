class Solution:
    def rob(self, nums: List[int]) :

        memo={}
        def maxrob(i):
            #returns max robbery , ith being first house
            if i>=len(nums):return 0
            if i in memo: return memo[i]
 
            maxm=nums[i]
            for j in range(i+2,len(nums)):maxm=max(maxm, nums[i]+maxrob(j))
            memo[i]=maxm
            return maxm

        maxm=0
        for i in range(len(nums)):maxm=max(maxm,maxrob(i))
        return maxm 

        