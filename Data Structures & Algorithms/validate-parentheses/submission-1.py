class Solution:
    def isValid(self, s: str) :
        seta={"(":")","[":"]","{":"}"}
        stack=[]
        for ele in s:
            if not stack:
                stack.append(ele)
                continue
            
            if stack[-1] in seta and ele not in seta and seta[stack[-1]]==ele : 
                stack.pop()
                continue
            stack.append(ele)
        if stack:return False
        return True
        