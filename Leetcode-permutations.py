'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
'''


from itertools import permutations

class Solution:
    '''
    Runtime
0
ms
Beats
100.00%

Memory
19.17
MB
Beats
99.51%

    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        values = list(permutations(nums))
        print(values)
        return values


class Solution:
    '''
    Runtime
1
ms
Beats
44.80%

Memory
19.46
MB
Beats
66.32%

    '''
    # Using backtracking
    def permute(self, nums: List[int]) -> List[List[int]]:

        final_list = []

        def bt(path):

            if len(path) == len(nums):
                # print("path list size is equal to nums size...")
                final_list.append(path[:])
                return

            for num in nums:
                if num in path:
                    # print(f"considering::: {num} but already in path")
                    continue
                # print(f"considering::: {num}, appended and backtracking")
                path.append(num)
                bt(path)

                # print(f"before poping::: {path}")
                path.pop()
                # print(f"after poping::: {path}")

        bt([])
        print(final_list)
        return final_list