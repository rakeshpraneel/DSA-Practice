'''
Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
'''


class Solution:
    '''
    Runtime 9 ms Beats 94.65%
    Memory 19.72 MB Beats 78.74%
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        temp = [[0 ] *n for _ in range(m)]
        temp[0][0] = grid[0][0]

        # Adding first row and column values
        for i in range(1,n):
            temp[0][i] = temp[0][ i -1] + grid[0][i]
        for i in range(1,m):
            temp[i][0] = temp[ i -1][0] + grid[i][0]

        # Fill other positions
        for i in range(1 ,m):
            for j in range(1 ,n):
                temp[i][j] = grid[i][j] + min(temp[ i -1][j] ,temp[i][ j -1])

        return temp[ m -1][ n -1]