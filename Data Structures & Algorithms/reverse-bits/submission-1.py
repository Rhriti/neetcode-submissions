class Solution:
    def reverseBits(self, n: int) :

        nnew=0
        j=1
        for i in range(31,-1,-1):
            if (n & j)!=0:
                nnew+=2**i
            j=j<<1
        return nnew

        