class Solution:
    def combinationSum2(self, cand: List[int], target: int):
        cand.sort()
        final=[]
        def f(i,target,curr):
            if target==0: 
                final.append(curr[::])
                return 
            if target<0:return 
            if i==len(cand):return 

            for j in range(i,len(cand)):
                #base condition
                if j>i and cand[j]==cand[j-1]:continue

                curr.append(cand[j])
                f(j+1,target-cand[j],curr)
                curr.pop()
        f(0,target,[])
        return final
                


        
        