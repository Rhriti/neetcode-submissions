class Solution:
    def hammingWeight(self, n: int) :
        c=0
        mask=1
        for _ in range(32):
            if (n & mask)!=0:
                c+=1
            mask=mask<<1
        return c
        