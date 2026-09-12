class Solution:
    def solve(self, board: List[List[str]]) :
        q=[]
        v=set()
        for c in range(len(board[0])):
            q.append([-1,c])
            q.append([len(board),c])
            v.add((-1,c))
            v.add((len(board),c))
        for r in range(len(board)):
            q.append([r,-1])
            q.append([r,len(board[0])])
            v.add((r,-1))
            v.add((r,len(board[0])))

    
        while q:
            temp_q=[]
            for ele in q:
                for dr,dc in [[-1,0],[1,0],[0,1],[0,-1]]:
                    r=ele[0]+dr
                    c=ele[1]+dc
                    if 0<=r<len(board) and 0<=c<len(board[0]) and (r,c) not in v and board[r][c]=="O":
                        print('O near river',r,c)
                        v.add((r,c))
                        temp_q.append([r,c])
            q=temp_q

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O" and (i,j) not in v:
                    board[i][j]="X"
        
        























        