import math
class Solution:
    def reverseBits(self, n: int) :

        nnew=0
        j=1
        for i in range(31,-1,-1):
            if (n & j)!=0:
                nnew+=math.pow(2,i)
            j=j<<1
        return int(nnew)

        