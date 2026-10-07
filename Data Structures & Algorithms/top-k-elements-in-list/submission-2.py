from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        g=Counter(nums)
        fre=[[] for _ in range(len(nums)+1)]

        for key,v in g.items():
            fre[v].append(key)
        final=[]
        for i in range(len(fre)-1,-1,-1):
            if fre[i]:
                for ele in fre[i]:
                    final.append(ele)
                    k-=1
                    if k==0:return final



        