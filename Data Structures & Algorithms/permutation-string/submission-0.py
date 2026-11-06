from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #base conditoin
        if len(s1)>len(s2):return False
        s1_fm=Counter(s1)
        
        j=0
        curr_fm=Counter(s2[:len(s1)])
        if curr_fm==s1_fm:return True
        for i in range(len(s1),len(s2),1):
            curr_fm[s2[j]]-=1
            if curr_fm[s2[j]]==0:del curr_fm[s2[j]]
            curr_fm[s2[i]]+=1
            if curr_fm==s1_fm:return True
            j+=1
        return False





        