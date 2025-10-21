'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current_iter = max_overall = nums[0]
        for num in nums[1:]:
            max_current_iter = max(num, num+max_current_iter)
            max_overall = max(max_overall, max_current_iter)
        return max_overall
