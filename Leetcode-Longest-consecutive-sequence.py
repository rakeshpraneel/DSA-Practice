'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
'''
class Solution:
    def longestConsecutive_besttimecomplexity(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        max_ = 0
        # print(nums)
        for val in nums:
            if not val - 1 in nums:
                # print(f"smallest value for now::: {val}")
                smallest_val = val
                while smallest_val in nums:
                    # print(f"smallest value found::: {smallest_val}")
                    smallest_val += 1
                max_ = max(max_, smallest_val - val)
        return max_
    def longestConsecutive_bestspacecomplexity(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        total_len = len(nums)
        max_ = 0
        counter = 1
        print(nums)
        for i in range(1,total_len):
            if nums[i]-nums[i-1] == 1:
                counter += 1
                print(f"counter::: {counter}")
            elif nums[i]-nums[i-1] > 1:
                max_ = max(max_,counter)
                counter = 1
        return max(max_,counter)