'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
'''

from collections import Counter

class Solution:
    '''
    Runtime 10 ms Beats 7.35%
    Memory 19.36 MB Beats 36.98%
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        temp = []
        for values in board:
            c = Counter(v for v in values if v != ".")
            # print(c)
            for count in c.values():
                if count > 1:
                    return False
        for col in range(9):
            c = Counter(board[row][col] for row in range(9) if board[row][col] != ".")
            # print(c)
            for count in c.values():
                if count > 1:
                    return False
        box = []
        for row in range(0 ,9 ,3):
            for col in range(0 ,9 ,3):
                for i in range(row ,ro w +3):
                    for j in range(col ,co l +3):
                        box.append(board[i][j])
                print(box)
                c = Counter(elements for elements in box if elements != ".")
                print(c)
                for count in c.values():
                    if count > 1:
                        return False
                box = []
        return True



