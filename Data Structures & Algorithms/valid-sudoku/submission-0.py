from collections import defaultdict 
class Solution:
    def isValidSudoku(self, board: List[List[str]]):
        rows=defaultdict(set)
        cols=defaultdict(set)
        grid=defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                ele=board[r][c]
                #base
                if ele==".":continue

                if ele in rows[r] or ele in cols[c] or ele in grid[(r//3,c//3)]:
                    return False 
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grid[(r//3,c//3)].add(board[r][c])
        return True

        