class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        
        res= []
        
        board = [["."]*n for i in range(n)]
        
        # place queens in a row then look at how 
        # you can place another queen in the next row
        
        def backtrack(r):
            
            # check if r has reached end of board
            if r == n :
                # copy the result and return
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                # check if positions are already part of
                # a placed queens mooves
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                       
            # else add the positions associated with
            # a particular Queen and update sets
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                # move onto next row
                backtrack(r + 1)
                
                # clean up set for next iteration
                # and seeing if other ways of placing the same queen exists
                
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
                
        # start from row 0
        backtrack(0)
        
        return res
                
                

            
        