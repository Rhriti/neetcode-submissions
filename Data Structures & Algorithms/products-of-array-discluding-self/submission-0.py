class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix
        #suffix
        pre=1
        pre_arr=[]
        for ele in nums:
            pre_arr.append(pre)
            pre=pre*ele
        
        post_arr=[1]*len(nums)
        post=1
        for i in range(len(nums)-1,-1,-1):
            post_arr[i]=post
            post=post*nums[i]
        
        result=[]
        for i in range(len(nums)):
            result.append(pre_arr[i]*post_arr[i])
        return result


        