class Solution:
    def subsets(self, nums: List[int]) :

        def subset(i):
            if i==len(nums)-1: return [[],[nums[-1]]]
            future=subset(i+1)
            arr=[]
            for ele in future:
                copyele=ele.copy()
                ele.append(nums[i])
                arr.append(ele)
                arr.append(copyele)
            return arr

        return subset(0)
            
        