class Solution:
    def lengthOfLongestSubstring(self, s: str) :
        if s=="":return 0
        index={}
        i=j=0
        maxs=1
        while j<len(s):
            if s[j] in index:
                maxs=max(maxs,j-i)
                pos=index[s[j]]
                for i in range(i,pos+1):
                    del index[s[i]]
                i+=1

            index[s[j]]=j
            j+=1
            maxs=max(maxs,j-i)
        return maxs
