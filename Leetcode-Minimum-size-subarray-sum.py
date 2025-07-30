class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        max_ = len(nums)
        start_pointer = 0
        pivot_pointer = 0
        iter_sum = 0
        pivot_flag = False
        while pivot_pointer < len(nums) and start_pointer < len(nums):
            # print(f"****" * 10)
            # print(f"minimum length obtained as of now::: {max_}")
            # print(f"start pointer::: {start_pointer}")
            # print(f"end pointer::: {pivot_pointer}")
            if not pivot_flag:
                iter_sum += nums[start_pointer]
            # print(f"current sum::: {iter_sum}")
            if iter_sum < target:
                start_pointer += 1
                pivot_flag = False
            else:
                # print("expected sum found....")
                max_ = min(max_,max(start_pointer,pivot_pointer)-min(start_pointer,pivot_pointer)+1)
                iter_sum -= nums[pivot_pointer]
                pivot_pointer += 1
                # print(f"current sum::: {iter_sum}")
                pivot_flag = True
        return max_ if pivot_pointer > 0 else 0