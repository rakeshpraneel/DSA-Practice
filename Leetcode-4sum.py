'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

class Solution:
    '''
    Runtime
711
ms
Beats
8.23%

Memory
19.38
MB
Beats
54.86%

    '''
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        first = 0
        final = []
        while (first<len(nums)-3):
            # print(f"first position:: {first}")
            second=first+1
            if first > 0 and nums[first] == nums[first-1]:
                first+=1
                continue
            while (second<len(nums)-2):
                if second > first+1 and nums[second] == nums[second-1]:
                    second+=1
                    continue
                left = second + 1
                right = len(nums)-1
                while(left < right):
                    if nums[first]+nums[second]+nums[left]+nums[right] == target:
                        final.append([nums[first],nums[second],nums[left],nums[right]])
                        right -= 1
                        left += 1
                    elif nums[first]+nums[second]+nums[left]+nums[right] > target:
                        right -= 1
                        continue
                    elif nums[first]+nums[second]+nums[left]+nums[right] < target:
                        left += 1
                        continue
                    # if left < right and nums[left] == nums[left-1]:
                    #     left += 1
                    #     continue
                    # if left < right and nums[right] == nums[right+1]:
                    #     right -= 1
                    #     continue
                    # if left < right and nums[left] == nums[left-1]:
                    #     left +=1
                second += 1
            first += 1
        # To remove duplicates we tried using set but list of list cannot be directly converted
        # to set due to hashable object
        final = list(map(list,set(map(tuple,final))))
        print(final)
        return final
