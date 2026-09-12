class MinStack:

    def __init__(self):
        self.arr=[]
        
    def push(self, val: int) -> None:
        if not self.arr: self.arr.append([val,val])
        else:
            self.arr.append([val,min(val,self.arr[-1][1])])
        
    def pop(self):
        self.arr.pop()


    def top(self):
        return self.arr[-1][0]
        

    def getMin(self) :
        return self.arr[-1][1]
        
