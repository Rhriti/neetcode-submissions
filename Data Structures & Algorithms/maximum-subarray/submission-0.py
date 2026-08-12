class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        cm=om=-float('inf')
        for j in range(len(nums)):
            cm+=nums[j]
            if nums[j]>cm:
                cm=nums[j]
                i=j
            om=max(om,cm)
        return om
        