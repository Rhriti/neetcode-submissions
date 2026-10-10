class Solution:
    def longestConsecutive(self, nums: List[int]) :
        s=set(nums)
        maxm=0
        for ele in nums:
            if ele-1 in s:continue
            count=0
            itr=ele
            while itr in s:
                count+=1
                itr=itr+1
            maxm=max(maxm,count)
        return maxm


        