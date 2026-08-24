import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) :
        if h==len(piles): return max(piles)
        i=1
        j=max(piles)

        while j>=i:
            midspeed=(i+j)//2
            time=0
            for ele in piles: time+=math.ceil(ele/midspeed)
            if time>h: i=midspeed+1
            else:j=midspeed-1
        return i
        