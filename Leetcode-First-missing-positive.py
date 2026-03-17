'''
First Missing Positive

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


'''
class Solution:
    '''
    Runtime 53ms Beats 47.59%
    Memory 30.75MB Beats 92.04%

    '''
    def firstMissingPositive(self, nums: List[int]) -> int:
        start = 1
        length = len(nums)
        print(length)
        for i in range(length):
            while 1<= nums[i] <= length and nums[i] != nums[nums[i] - 1]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1

        # while start:
        #     if start not in nums:
        #         return start
        #     else:
        #         start +=1