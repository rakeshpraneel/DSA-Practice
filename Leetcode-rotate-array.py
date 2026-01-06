'''
Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

'''
Observation: using reversed() is efficient in both time and memory usage comparing to slice
'''

class Solution:
    '''
    Runtime 8ms Beats 28.31%
    Memory 24.36MB Beats 88.34%
    '''
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k>len(nums):
            k = k%len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        print(nums)

class Solution:
    '''
    Runtime 4ms Beats 58.13%
    Memory 24.25MB Beats 97.14%
    '''
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k>len(nums):
            k = k%len(nums)
        nums[:] = reversed(nums)
        nums[k:] = reversed(nums[:k])
        nums[:k] = reversed(nums[k:])
        print(nums)