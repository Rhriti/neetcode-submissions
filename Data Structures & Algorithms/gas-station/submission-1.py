class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]):
        
        i=0
        currgas=0
        counter=0
        while i<2*len(gas):
            counter+=1
            index=i%len(gas)
            currgas+=gas[index]
            currgas-=cost[index]
            if currgas<0:
                counter=0
                currgas=0
            else:
                if counter==len(gas):
                    return  (i+1)%len(gas)
            i+=1
        return -1 
        