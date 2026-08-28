class Solution:
    def insert(self, interval: List[List[int]], newinterval: List[int]):
        interval.append(newinterval)
        interval.sort()
        arr=[]
        for ele in interval:
            if not arr: 
                arr.append(ele)
                continue
            if arr[-1][0]<=ele[0]<=arr[-1][1]:
                arr[-1][0]=min(arr[-1][0],ele[0])
                arr[-1][1]=max(arr[-1][1],ele[1])
            else:
                arr.append(ele)
        return arr
        
        


        
