class Solution:
    def reverseBits(self, n: int) :

        nnew=0
        for i in range(31,-1,-1):
            if (n & 1)==1:
                nnew+=2**i
            n=n>>1
        return nnew

        