'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
'''

from itertools import permutations

class Solution:
    '''
    Runtime
15
ms
Beats
18.91%

Memory
24.54
MB
Beats
7.41%
    '''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        values = list(permutations(nums))
        # print(set(values))
        return list(set(values))



class Solution:
    # backtracking
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        final_list = []
        def bt(p_list):

            if len(p_list) == len(nums):
                # print("length matches combination generated...")
                if p_list not in final_list:
                    final_list.append(p_list[:])
                return

            for num in nums:
                if nums.count(num) == p_list.count(num):
                    # print(f"{num} has already been pushed to p_list")
                    # print(f"current plist {p_list}")
                    continue

                p_list.append(num)

                bt(p_list)
                # print(f"p list before poping::: {p_list}")
                p_list.pop()
                # print(f"p list after poping::: {p_list}")

        bt([])
        # print(final_list)
        return final_list


