from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int):
        freq_map=defaultdict(int)
        maxl=0
        i=0
        for j in range(len(s)):
            freq_map[s[j]]+=1
            max_freq=max(freq_map.values())
            left=(j-i+1)-max_freq
            if left<=k:
                maxl=max(maxl,j-i+1)
                continue
            else:
                while left>k:
                    freq_map[s[i]]-=1
                    if freq_map[s[i]]<0: del freq_map[s[i]]
                    i+=1
                    left=(j-i+1)-max(freq_map.values())
        return maxl


        