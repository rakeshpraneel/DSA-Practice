'''
Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.
'''


# Solving by DP method
class Solution:
    '''
    Runtime
1687
ms
Beats
16.90%

Memory
20.03
MB
Beats
66.73%

    '''
    def jump(self, nums: List[int]) -> int:

        dp = [float('inf')]*len(nums)
        dp[0] = 0
        print(dp)

        for i in range(len(nums)):

            for j in range(i+1,min(len(nums),i+nums[i]+1)):

                dp[j] = min(dp[j],1+dp[i])

        print(dp)

        return dp[-1]

# Solving by greedy method
class Solution:
    '''
    Runtime
10
ms
Beats
29.02%

Memory
19.89
MB
Beats
98.94%

    '''
    def jump(self, nums: List[int]) -> int:
        far = 0
        # far = num[0]
        i = 0
        jump = 0
        current_index = 0
        while(i<len(nums)-1):
            far = max(far,i+nums[i])
            # print(f"position:: {i}")
            # print(f"value:: {nums[i]}")
            # print(f"farthest distance as of now::: {far}")
            if far == len(nums)-1:
                jump += 1
                i = len(nums)
            elif current_index == i:
                jump+=1
                current_index = far
                # print(f"current index matches with i {i}")
            i+=1
            # jump += 1
        # print(jump)
        return jump
