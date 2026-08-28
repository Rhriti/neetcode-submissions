class Solution:
    def insert(self, interval: List[List[int]], newinterval: List[int]):
        #base
        if len(interval)==0: return [newinterval]

        i=0
        j=len(interval)-1
        while j>=i:
            mid=(i+j)//2
            midele=interval[mid][0]
            if newinterval[0]<=midele: j=mid-1
            else: i=mid+1
        interval.insert(i,newinterval)

        j=i=0
        while j<=len(interval)-1:
            if interval[i][0]<=interval[j][0]<=interval[i][1]:
                interval[i][0]=min(interval[i][0],interval[j][0])
                interval[i][1]=max(interval[i][1],interval[j][1])
            else:
                i+=1
                interval[i]=interval[j]
            j+=1
        
        del interval[i+1:]
        return interval
                
        


    
                

                

                



            