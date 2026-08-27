class Solution:
    def combinationSum(self, nums: List[int], target: int):

        allcomb=[]
        def backtrack(i,target,comb):
            if target<0:return
            if target==0:
                allcomb.append(comb.copy()) 
                return 
            if i==len(nums): return 
            comb.append(nums[i])
            backtrack(i,target-nums[i],comb)
            comb.pop()
            backtrack(i+1,target,comb)

        backtrack(0,target,[])

        return allcomb

        