class Solution:
    def findMin(self, nums: List[int]):
        i=0
        j=len(nums)-1
        minm=float('inf')
        while i<j:
            mid=(i+j)//2
            ele=nums[mid]
            minm=min(minm,ele)
            if ele>nums[j]:
                i=mid+1
            else:
                j=mid
        return min(minm,nums[i])
        