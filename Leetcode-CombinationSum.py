'''
Combination Sum
Solved
Medium
Topics
premium lock icon
Companies
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

'''


class Solution:
    '''
    Runtime
    4
    ms
    Beats
    83.59%

    Memory 19.53 MB
Beats
64.60%

    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        final_list = []

        def bt(current_list, remain, start_index):

            if remain == 0:
                # print("finallist ",final_list)
                final_list.append(current_list[:])
                # print('returning from result found...')
                return

            if remain < 0:
                # print("returning from negative result...")
                return

            for i in range(start_index, len(candidates)):
                current = candidates[i]
                current_list.append(current)
                bt(current_list, remain - current, i)

                # print(current_list)
                current_list.pop()
                # print(f"after poping::: {current_list}")

        bt([], target, 0)
        print(final_list)
        return final_list
