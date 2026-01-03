'''
Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
'''

class Solution:
    '''
    Runtime 0 ms Beats 100.00%
    Memory 17.19 MB Beats 99.04%
    '''
    def myPow(self, x: float, n: int) -> float:
        result = 1
        times = abs(n)
        while times > 0:
            if times%2 != 0:
                result *= x
            x *= x
            # print(f"result:: {result}")
            # print(f"x:: {x}")
            times = times//2
        return result if n>0 else 1/result