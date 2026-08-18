class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) :
        alphadict={c:[] for c in 'abcdefghijklmnopqrstuvwxyz'}
        for ele in wordDict:alphadict[ele[0]].append(ele)


        def check(ele,i):
            #base condition
            if len(ele)>len(s)-i: return False

            for ch in ele:
                if ch!=s[i]: return False
                i+=1
            return True
        memo1={}
        def WB(i):
            if i in memo1: return memo1[i]
            if i>=len(s):return True
            if not alphadict[s[i]]: return False

            
            f=False
            for ele in alphadict[s[i]]:
                if check(ele,i):
                    f =f or WB(i+len(ele))
            memo1[i]=f
            return f
        
        return WB(0)





        