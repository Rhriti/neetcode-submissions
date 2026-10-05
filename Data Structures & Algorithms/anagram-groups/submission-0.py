from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g=defaultdict(list)
        for i in range(len(strs)):
            ele=strs[i]
            freq_map=[0 for _ in range(26)]
            for j in range(len(ele)):freq_map[ord(ele[j])-ord('a')]+=1
            g[tuple(freq_map)].append(strs[i])
        final=[]
        for v in g.values():
            if v:final.append(v)
        return final

        
        