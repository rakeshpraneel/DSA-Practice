'''
Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [float('inf') ] *len(nums)
        dp[0] = 0

        for i in range(len(nums)):
            for j in range( i +1, min(len(nums) , i +nums[i ] +1)):
                dp[j] = min(dp[j], 1+ dp[i])

        print(dp)
        return True if dp[-1] != float('inf') else False


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        far = 0
        current_index = 0
        i = 0
        while (i < len(nums)):
            # print(f"farthest position can go is {far}")
            if i > far:
                i = len(nums)
                return False
            far = max(far, i + nums[i])
            i += 1
            # print(f"position is {i}")

        return True