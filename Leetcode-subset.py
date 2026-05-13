'''
Subsets:
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''

class Solution:
    '''
    Runtime
0
ms
Beats
100.00%

Memory
19.40
MB
Beats
66.78%

    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []

        def bt(start ,temp):

            '''
            It doesn't require any return since the loop inside backtracking ends naturally through incrementing i at every
            recurrsion.
            '''

            # if temp in subset:
            #     # print(f"temp found in subset, temp:: {temp} & subset:: {subset}")
            #     return
            # current = temp.copy()
            subset.append(temp[:])
            # print(f"subset value::: {subset}")

            for i in range(start ,len(nums)):

                temp.append(nums[i])
                # print(f"temp value....{temp}")
                bt( i +1 ,temp)

                # print(f"before poping....{temp}")
                temp.pop()
                # print(f"after poping....{temp}")

        bt(0 ,[])
        return subset