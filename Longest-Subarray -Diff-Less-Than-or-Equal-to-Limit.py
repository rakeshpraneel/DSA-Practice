'''
Longest Subarray with Absolute Diff Less Than or Equal to Limit

You are given an integer array nums and an integer limit.
Return the length of the longest contiguous subarray such that the absolute difference between any two elements in this subarray is less than or equal to limit

Input: nums = [8, 2, 4, 7], limit = 4
Output: 2
Explanation: The subarray [2, 4] or [4, 7] is valid. But [2, 4, 7] is not since 7 - 2 = 5 > 4.

Input: nums = [10, 1, 2, 4, 7, 2], limit = 5
Output: 4
Explanation: The subarray [2, 4, 7, 2] has max - min = 5 and is the longest.

nums = [1, 2, 3, 4, 5]
limit = 3
# Valid subarrays: [1,2,3,4], [2,3,4,5]
# Answer: 4

nums = [8, 2, 4, 7]
limit = 4
# [2,4], [4,7] are valid → length = 2
# [2,4,7] is invalid since 7 - 2 = 5
# Answer: 2

nums = [10, 1, 2, 4, 7, 2]
limit = 5
# Longest valid subarray: [2, 4, 7, 2]
# Answer: 4

nums = [5, 5, 5, 5]
limit = 0
# Every subarray valid (all diffs = 0)
# Answer: 4

nums = [1, 2, 3, 50, 4, 5]
limit = 3
# Longest valid: [1,2,3] or [4,5]
# Answer: 3

nums = [1, 6, 3, 5, 2]
limit = 5
# Max diff in entire array is 6 - 1 = 5
# Answer: 5

nums = [1, 100, 1, 100]
limit = 0
# No two different values allowed → only single element subarrays
# Answer: 1

nums = [1] * 10**5
limit = 0
# All same → whole array valid
# Answer: 100000

nums = [4, 7, 6, 7, 5, 6]
limit = 2
# Whole array is valid (max=7, min=4 → diff=3 > 2 → not valid)
# But [6,7,5,6] is valid
# Answer: 4

nums = [1000] * 50000 + [0] * 50000  # Half max, half min
limit = 1000

import random

# Case: maximum size, large difference
nums = [i for i in range(100000)]  # strictly increasing
limit = 1

### worst case scenario
nums = [1, 2] * 50000
limit = 10

nums = [5] * 100000
limit = 0

nums = list(range(50000))  # Larger array
limit = 1
'''

import time_calculator

@time_calculator.timer_function
def find_diff_subarray(input_val, max_diff):
    pivot_ptr = 0
    if max(input_val) - min(input_val) <= max_diff:
        return len(input_val)
    else:
        max_length_found = 0
    print(f"Initial maximum length found::: {max_length_found}")
    maximum_reserve = input_val[0]
    minimum_reserve = input_val[0]
    for current_ptr in range(1,len(input_val)):
        print(f"Current position::: {current_ptr}")
        maximum_reserve = max(maximum_reserve,input_val[current_ptr])
        minimum_reserve = min(minimum_reserve,input_val[current_ptr])
        if maximum_reserve - minimum_reserve <= max_diff:
            print(f"difference found within limit::: {input_val[pivot_ptr:current_ptr+1]}")
            max_length_found = max(max_length_found,current_ptr-pivot_ptr+1)
        while maximum_reserve - minimum_reserve > max_diff and pivot_ptr < current_ptr:
            print(f"condition not satisfied {input_val[pivot_ptr:current_ptr + 1]}, increasing pivot::: {pivot_ptr}")
            pivot_ptr += 1
            maximum_reserve = max(input_val[pivot_ptr:current_ptr+1])
            minimum_reserve = min(input_val[pivot_ptr:current_ptr+1])
        print(f"Max length found for this iteration::: {max_length_found}")
    return max_length_found


nums = list(range(50000))  # Larger array
limit = 1
answer = find_diff_subarray(nums,limit)
print(answer)