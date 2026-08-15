class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo={}
        def lcsDP(i,j):
            if i==len(text1) or j==len(text2):return 0
            if (i,j) in memo: return memo[(i,j)]

            maxlcs=-float('inf')
            if text1[i]==text2[j]:
                maxlcs=max(1+ lcsDP(i+1,j+1),maxlcs)
            else:
                maxlcs=max(max(lcsDP(i+1,j),lcsDP(i,j+1)),maxlcs)
            memo[(i,j)]=maxlcs
            return maxlcs
        
        return lcsDP(0,0)

            