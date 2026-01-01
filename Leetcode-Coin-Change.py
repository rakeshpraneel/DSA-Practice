'''
Problem Statement:

Coin Change
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
'''

'''
Logic Implemented - Reverse Iteration

i/p: coins = [2] and amount = 3
o/p:
amount planned to be filled:: 1
---------------
amount planned to be filled:: 2
coin in use:: 2
referring to 0 amount
min coin achieved for this turn  1
---------------
amount planned to be filled:: 3
coin in use:: 2
referring to 1 amount
min coin achieved for this turn  inf
---------------
[0, inf, 1, inf]
'''

class Solution:
    '''
    Runtime 720 ms Beats 75.11%
    Memory 17.52 MB Beats 97.91%
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        temp = [float(inf)] * (amount+1)
        temp[0] = 0
        for i in range(1,amount+1):
            # print(f"amount planned to be filled:: {i}")
            for coin in coins:
                if coin <= i:
                    # print(f"coin in use:: {coin}")
                    # print(f"referring to {i-coin} amount")
                    temp[i] = min(temp[i],temp[i-coin]+1)
                    # print("min coin achieved for this turn ",temp[i])
            # print("---"*5)
        # print(temp)
        return temp[-1] if temp[-1] != float(inf) else -1