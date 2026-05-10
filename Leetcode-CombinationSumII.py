'''
Combination Sum II
Solved
Medium
Topics
premium lock icon
Companies
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
'''



class Solution:
    '''
    Runtime
0
ms
Beats
100.00%

Memory
19.28
MB
Beats
97.15%

    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates = sorted(candidates)
        # print(candidates)
        final_list = []

        def bt(start_index, current_list, remaining):

            # print(f"current start index::: {start_index}")

            if remaining == 0:
                # print("Combination found....")
                if not current_list[:] in final_list:
                    final_list.append(current_list[:])
                # print(f"final list::: {final_list}")
                # final_list.append(current_list[:])
                return

            if remaining < 0:
                # print(f"inside found negative:: {current_list}")
                # print("remaining went negative....")
                return

            for i in range(start_index, len(candidates)):

                if i > start_index and candidates[i] == candidates[i - 1]:
                    # print("Found a possible duplicate candidate combination...")
                    # print(f"current list {current_list}")
                    # print(f"candidate index: {i} and candidate: {candidates[i]}")
                    continue

                current = candidates[i]
                current_list.append(candidates[i])

                bt(i + 1, current_list, remaining - candidates[i])

                # print(current_list)

                current_list.pop()
                # print("value poped")
                # print(current_list)

                if candidates[i] > remaining:
                    # print(f"candidate {candidates[i]} is > than remaining...so breaking")
                    break

        bt(0, [], target)
        # print(final_list)

        return final_list