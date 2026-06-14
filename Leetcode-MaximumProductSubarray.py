'''
Maximum Product Subarray
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
Note that the product of an array with a single element is the value of that element.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''


class Solution:
    '''
    Runtime
7
ms
Beats
39.84%

Memory
19.66
MB
Beats
97.16%

    '''
    def maxProduct(self, nums: List[int]) -> int:
        max_v = nums[0]
        min_v = nums[0]
        answer = nums[0]
        # print(f"For position {0}: max_value:{max_v}; min_value:{min_v}; answer:{answer}")
        for i in range(1,len(nums)):
            if nums[i] < 0:
                max_v,min_v = min_v,max_v
            max_v = max(nums[i],max_v*nums[i])
            min_v = min(nums[i],min_v*nums[i])

            answer = max(answer,max_v)
            # print(f"For position {i}: max_value:{max_v}; min_value:{min_v}; answer:{answer}")
        # print(answer)
        return answer