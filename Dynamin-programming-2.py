'''
House Robber
You can't rob two adjacent houses.

Return the maximum amount of money you can rob without alerting the police.

Input: [1, 2, 3, 1]
Output: 4
Explanation: Rob house 1 (money = 1) and house 3 (money = 3) → 1 + 3 = 4

Input: [2, 7, 9, 3, 1]
Output: 12
Explanation: Rob house 1 (2), skip 2 (7), rob 3 (9), skip 4 (3), rob 5 (1)
→ Total = 2 + 9 + 1 = 12

nums = []

nums = [5]
# Expected: 5 → Only one option

nums = [2, 3]
# Expected: 3 → Pick the larger of the two

nums = [5, 5, 5, 5]
# Expected: 10 → Rob 0 and 2, or 1 and 3

nums = [1, 100, 1]
# Expected: 100 → Rob the middle house

nums = [1, 2, 3, 4, 100]
# Expected: 104 → Rob 1, 3, and 4 (2 + 4 + 100)

nums = [1]*100000
# Expected: 50000 → Rob every other house

nums = list(range(1, 101))  # [1, 2, ..., 100]
# Expected: Rob 2 + 4 + 6 + ... + 100 = 2550
# Use even indices for max sum in this case
'''

import time_calculator

@time_calculator.timer_function
def find_max_could_rob_circular(input_val):
    '''
    Function for circular houses
    '''
    odd_max = 0
    total_houses = len(input_val)
    even_max = max(input_val[0],input_val[-1]) if total_houses%2 != 0 else 0
    for i in range(1,total_houses-1):
        if i % 2 == 0:
            even_max = even_max + input_val[i]
        else:
            odd_max = odd_max + input_val[i]
    return max(even_max, odd_max)

@time_calculator.timer_function
def find_max_could_rob(input_val):
    even_max = 0
    odd_max = 0
    for i in range(len(input_val)):
        if i % 2 == 0:
            even_max = even_max + input_val[i]
        else:
            odd_max = odd_max + input_val[i]
    return max(even_max,odd_max)

nums = list(range(1, 101))
answer = find_max_could_rob(nums)
print(answer)

answer = find_max_could_rob_circular(nums)
print(answer)