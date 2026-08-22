class Solution:
    def countBits(self, n: int):
        
        memo={}
        def dp_1(n):
            if n==0: return 0
            if n in memo: return memo[n]

            memo[n]=1+dp_1(n & n-1)
            return memo[n]
        
        arr=[]
        for ele in range(n+1):
            arr.append(dp_1(ele))
        return arr



        