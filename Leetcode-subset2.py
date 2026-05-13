'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
'''


class Solution:
    '''
    Runtime
3
ms
Beats
20.11%

Memory
19.42
MB
Beats
59.36%

    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        nums.sort()

        def bt(start, temp):

            # if temp not in subset:

            subset.append(temp[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                temp.append(nums[i])
                bt(i + 1, temp)

                temp.pop()
            # return

        bt(0, [])
        return subset
