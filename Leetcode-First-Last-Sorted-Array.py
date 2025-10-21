'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

'''


class Solution:
    '''
    Solved through binary search so that we can find without full iteration
    Time complexity: 0ms Beats 100%
    Space complexity: 19MB Beats 53.52%
    '''
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        return_val = [-1,-1]
        while low <= high:
            mid = (high+low)//2
            if nums[mid] == target:
                while low <= high:
                    low = low+1 if nums[low] < target else low
                    high = high-1 if nums[high] > target else high
                    if nums[low] == target:
                        return_val[0] = low
                    if nums[high] == target:
                        return_val[1] = high
                    if return_val[0] != -1 and return_val[1] != -1:
                        low = high+1
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return return_val




class Solution:
    '''
    Solved through iterating till greater value is meet
    Time complexity: 3ms Beats 7.35%
    Space complexity: 19.05MB Beats 53.52%
    '''
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return_val = [-1,-1]
        current_post = 0
        while current_post < len(nums):
            if nums[current_post] > target:
                return_val[1] = current_post-1 if return_val[0] != -1 else return_val[1]
                return return_val
            if nums[current_post] == target:
                return_val[0] = current_post if return_val[0] == -1 else return_val[0]
            current_post += 1
        return_val[1] = current_post-1 if return_val[0] != -1 else return_val[1]
        return return_val