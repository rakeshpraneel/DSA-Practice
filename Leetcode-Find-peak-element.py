'''
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
'''
class Solution:
    '''
    Time Complexity: Runtime 0 ms Beats 100.00%
    Space Complexity: 17.94 MB Beats 38.46%
    '''
    def findPeakElement(self, nums: List[int]) -> int:
        try:
            return nums.index(max(nums))
        except:
            return 0

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        try:
            return nums.index(max(nums))
        except:
            return 0