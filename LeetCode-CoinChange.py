'''
Coin Change
Solved
Medium
Topics
premium lock icon
Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''



class Solution:
    '''
    Runtime
447
ms
Beats
89.52%

Memory
19.56
MB
Beats
77.76%

    '''
    def coinChange(self, coins, amount) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # print(dp)

        for target in range(1, amount + 1):
            for coin in coins:
                if coin <= target:
                    # print(target)
                    # print(target-coin)
                    dp[target] = min(dp[target], 1 + dp[target - coin])

        return dp[amount] if dp[amount] != float('inf') else -1

obj = Solution()
print(obj.coinChange([1,2,3,45], 6))

