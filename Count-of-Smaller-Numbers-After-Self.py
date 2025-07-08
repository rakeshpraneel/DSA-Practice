'''
Problem: Count of Smaller Numbers After Self
LeetCode 315:
You are given an integer array nums, and you need to return an array result such that result[i] is the number of smaller elements to the right of nums[i].

Input: nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]

Explanation:
- 5 has two smaller elements after it: 2 and 1.
- 2 has one smaller: 1.
- 6 has one smaller: 1.
- 1 has none.

nums = [1, 2, 3, 4]
# Every element has 0 smaller elements to its right
# Expected: [0, 0, 0, 0]

nums = [4, 3, 2, 1]
# Every element has all remaining elements smaller
# Expected: [3, 2, 1, 0]

nums = [2, 2, 2, 2]
# No element is strictly smaller
# Expected: [0, 0, 0, 0]

nums = [1, 3, 2, 3, 1]
# Explanation:
# 1 → [3,2,3,1] → 0
# 3 → [2,3,1] → 2
# 2 → [3,1] → 1
# 3 → [1] → 1
# 1 → [] → 0
# Expected: [0, 2, 1, 1, 0]

import random
nums = [random.randint(1, 10000) for _ in range(100000)]
# You can check for performance or crash — correctness not easily verifiable manually.
'''
import bisect
import time_calculator
from sortedcontainers import SortedList

@time_calculator.timer_function
def find_count_array_sorted_container(input_val):
    '''
    solving using bisect module
    '''
    count_list = []
    container_obj = SortedList([])
    for current_ptr in range(len(input_val)-1,-1,-1):
        # print(f"current position::: {current_ptr} and value::: {input_val[current_ptr]}")
        count_list.append(bisect.bisect_left(container_obj,input_val[current_ptr]))
        container_obj.add(input_val[current_ptr])
        # empty_list.insert(count_list[len(input_val)-current_ptr-1],input_val[current_ptr])
        # print(f"counter list::: {count_list}")
        # print(f"additional list::: {empty_list}")
    return count_list

@time_calculator.timer_function
def find_count_array(input_val):
    '''
    solving using bisect module
    '''
    empty_list = []
    count_list = []
    for current_ptr in range(len(input_val)-1,-1,-1):
        # print(f"current position::: {current_ptr} and value::: {input_val[current_ptr]}")
        count_list.append(bisect.bisect_left(empty_list,input_val[current_ptr]))
        empty_list.insert(count_list[len(input_val)-current_ptr-1],input_val[current_ptr])
        # print(f"counter list::: {count_list}")
        # print(f"additional list::: {empty_list}")
    return count_list

import random
nums = [random.randint(1, 10000) for _ in range(100000)]
answer = find_count_array(nums)
print(answer[::-1])
answer = find_count_array_sorted_container(nums)
print(answer[::-1])
