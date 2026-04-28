'''
-4,-1,1,2
'''

class Solution:
    '''
    Solution by chatgpt which beats time complexity
    '''
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                # update closest
                if abs(target - curr_sum) < abs(target - closest):
                    closest = curr_sum

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum  # exact match

        return closest

class Solution:
    '''
    Mine, fails for 1 test case on time complexity
    '''
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        i = 0
        j = i + 1
        min_ = float(inf)
        answer = 0
        while i < j:
            # print(f"i value {i}")
            j = i + 1
            while j < len(nums) - 1:
                # print(f"j value {j}")
                for k in range(j + 1, len(nums)):
                    # print(f"combination of i,j,k value {i},{j},{k}")
                    sum_ = nums[i] + nums[j] + nums[k]
                    # print(f"Sum obtained:: {sum_}")
                    current = target - sum_ if target > sum_ else sum_ - target
                    # print(f"Current diff:: {current}")
                    # print(f"Min diff:: {min_}")
                    if current < min_:
                        answer = sum_
                        min_ = current
                # print("***"*10)
                j += 1
            i += 1
        return answer

