class Solution:
    def threeSum(self, nums: List[int]):

        nums.sort()
        final=[]
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            target=-nums[i]

            if i>0 and nums[i]==nums[i-1]:continue
            while j<k:
                #base condition for duplicates
                if j>i+1 and nums[j]==nums[j-1]:
                    j+=1
                    continue
                if k<len(nums)-1 and nums[k]==nums[k+1]:
                    k-=1
                    continue

                curr=nums[j]+nums[k]
                if curr==target: 
                    final.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                else:
                    if curr>target:
                        k-=1
                    else:
                        j+=1
        return final



        