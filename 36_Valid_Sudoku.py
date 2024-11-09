class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # create a dictionary for each row, column and box, then create a set for each of them to save the elements in current row, col and box
        row_dict = {0:set(), 1:set(), 2:set(), 3:set(), 4:set(), 5:set(), 6:set(), 7:set(), 8:set()}
        col_dict = {0:set(), 1:set(), 2:set(), 3:set(), 4:set(), 5:set(), 6:set(), 7:set(), 8:set()}
        box_dict = {0:{0:set(), 1:set(), 2:set()}, 1:{0:set(), 1:set(), 2:set()}, 2:{0:set(), 1:set(), 2:set()}}

        # iterate through the matrix and store the number elements into particular dictionary of sets
        # if the element already exist in row, col or box, return False
        for r in range(0, 9):
            x = r//3
            for c in range(0, 9):
                y = c//3
                if board[r][c] != ".":
                    if board[r][c] not in row_dict[r]:
                        row_dict[r].add(board[r][c])
                    else:
                        return False
                    
                    if board[r][c] not in col_dict[c]:
                        col_dict[c].add(board[r][c])
                    else:
                        return False
                    
                    if board[r][c] not in box_dict[x][y]:
                        box_dict[x][y].add(board[r][c])
                    else:
                        return False
        
        return True
