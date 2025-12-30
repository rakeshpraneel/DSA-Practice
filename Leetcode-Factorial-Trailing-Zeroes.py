'''
Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0


'''


class Solution:
    '''
    Runtime 4 ms
    Beats 23.96%
    -------------
    Memory 17.18 MB
    Beats 96.60%
    '''
    def trailingZeroes(self, n: int) -> int:
        return_data = int(n/5)
        n = n/5
        while n >= 5:
            return_data += int(n/5)
            n = int(n/5)
        return return_data