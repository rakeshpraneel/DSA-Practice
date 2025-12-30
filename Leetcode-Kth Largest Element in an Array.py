'''
MEDIUM

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

class Solution:
    '''
    Runtime
    51 ms
    Beats
    84.47%

    Memory
    28.76 MB
    Beats
    44.27%
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(list(tuple(nums)), reverse=True)
        return nums[k-1]