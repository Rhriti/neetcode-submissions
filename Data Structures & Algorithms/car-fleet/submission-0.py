class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) :
        pos_time=[]
        for i in range(len(speed)):
            time=(target-position[i])/speed[i]
            pos_time.append((position[i],time))
        pos_time.sort()
        
        fleet=1
        currtime=pos_time[-1][1]
        for i in range(len(pos_time)-2,-1,-1):
            if pos_time[i][1]<=currtime:
                continue
            else:
                fleet+=1
                currtime=pos_time[i][1]
        return fleet






        