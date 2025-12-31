'''
House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

'''


class Solution:
    '''
    Runtime 0 ms Beats 100.00%
    Memory 17.20 MB Beats 97.45%
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[-1]
        temp = [0]*len(nums)
        temp[0] = nums[0]
        temp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            temp[i] = max(temp[i-1],temp[i-2]+nums[i])
        return temp[-1]