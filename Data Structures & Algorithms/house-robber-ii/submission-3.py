class Solution:
    def rob(self, nums: List[int]):
        n=len(nums)
        if n==1:return nums[0]
        if n==2:return max(nums[0],nums[1])

        memo={}
        def f(i,j):
            if i>j:return 0
            if (i,j) in memo:return memo[(i,j)]
            
            memo[(i,j)]=max(nums[i]+f(i+2,j),f(i+1,j))
            return memo[(i,j)]
        
        return max(f(1,n-1),nums[0]+f(2,n-2))
        