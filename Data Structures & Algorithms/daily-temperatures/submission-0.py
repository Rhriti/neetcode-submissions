class Solution:
    def dailyTemperatures(self, temp: List[int]):
        #monoto dec stack
        stack=[(temp[0],0)] #(ele,index)
        dist=[0 for _ in range(len(temp))]
        for i in range(1,len(temp)):
            if temp[i]<=stack[-1][0]:stack.append((temp[i],i))
            else:
                while stack and temp[i]>stack[-1][0]:
                    out=stack.pop()
                    dist[out[1]]=i-out[1]
                stack.append((temp[i],i))
        
        return dist 


        