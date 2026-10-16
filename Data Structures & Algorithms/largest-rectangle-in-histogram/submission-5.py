class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        PSE=[-1]*n
        NSE=[n]*n
        mono_stack=[]

        #monotonic increasing stack
        for i in range(n):
            if not mono_stack:
                mono_stack.append(i)
                continue
            while mono_stack and heights[i]<=heights[mono_stack[-1]]:
                out=mono_stack.pop()
                NSE[out]=i
            if mono_stack:
                PSE[i]=mono_stack[-1]
            mono_stack.append(i)

        for i in range(n):
            NSE[i]+=1
            PSE[i]+=1
        
        maxm=0
        for i in range(n):maxm=max(maxm, heights[i]*(NSE[i]-PSE[i]-1))
        return maxm

        



        