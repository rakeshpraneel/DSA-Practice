'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
'''

class Solution:
    '''
    Runtime
3
ms
Beats
72.76%

Memory
20.85
MB
Beats
29.42%
    '''
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        print(counter)
        for key, val in counter.items():
            if val == 1:
                return key