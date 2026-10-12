class Solution:
    def twoSum(self, numbers: List[int], target: int):
        i=0
        j=len(numbers)-1
        while j>i:
            ele=numbers[i]+numbers[j]
            if ele==target:return [i+1,j+1]
            if ele>target:
                j-=1
            else:
                i+=1
