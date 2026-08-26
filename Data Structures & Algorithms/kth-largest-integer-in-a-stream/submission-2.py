import heapq as hq 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        hq.heapify(self.nums)
        while len(self.nums)>self.k:hq.heappop(self.nums)
        
    def add(self, val: int) :
        hq.heappush(self.nums,val)
        if len(self.nums)>self.k:
            hq.heappop(self.nums)
        return self.nums[0]
        
