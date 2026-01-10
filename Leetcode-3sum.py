'''
3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''



class Solution:
    '''
    Runtime 615 ms Beats 36.96%
    Memory 22.56 MB Beats 5.11%
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # print(nums)
        return_list = []
        i = 0
        while i<len(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            # print("---"*5)
            answer = nums[i]
            j = i+1
            k = len(nums)-1
            # print("i value is ",answer)
            while(j<k):
                # print("j value is ",nums[j])
                # print("k value is ",nums[k])
                # print(answer+nums[j]+nums[k])
                if answer + nums[j] + nums[k] > 0:
                    k -= 1
                elif answer + nums[j] + nums[k] == 0:
                    # print("sum found....",[answer,nums[j],nums[k]])
                    return_list.append([answer,nums[j],nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    # Skip duplicate right
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j +=1
                    k -= 1
                else:
                    j += 1
                # print(return_list)
            i+=1
        # print(return_list)
        return return_list


class Solution:
    '''
    This fails for few test cases with TLE
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        return_list = []
        for first in range(len(nums)):
            for second in range(first+1,len(nums)):
                for third in range(second+1,len(nums)):
                    final_list = [nums[first],nums[second],nums[third]]
                    if nums[first] + nums[second] + nums[third] == 0 and final_list not in return_list:
                        return_list.append(final_list)
                        # print(return_list)
        print(return_list)
        return return_list