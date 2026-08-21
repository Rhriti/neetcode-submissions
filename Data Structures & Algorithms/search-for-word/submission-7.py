class Solution:
    def exist(self, board: List[List[str]], word: str) :

        def WS(r,c,i,path):
            if board[r][c]!=word[i]: return False
            if (r,c) in path: return False
            if i==len(word)-1:return True
            path.add((r,c))

            t=False
            if r+1<len(board):
                t=t or WS(r+1,c,i+1,path)
             
            if r-1>=0:
                t=t or WS(r-1,c,i+1,path)
            
            if c+1<len(board[0]):
                t=t or WS(r,c+1,i+1,path)
        
            
            if c-1>=0:
                t=t or WS(r,c-1,i+1,path)
            
            path.remove((r,c))
            return t
        
        t=False
        for i in range(len(board)):
            for j in range(len(board[0])):
                path=set()
                t=t or WS(i,j,0,path)
        return t




        