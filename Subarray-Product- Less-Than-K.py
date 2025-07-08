'''
 Problem: Subarray Product Less Than K
Given an array of positive integers nums and an integer k,
return the number of contiguous subarrays where the product of all elements is strictly less than k.

Input:
nums = [10, 5, 2, 6]
k = 100
Output: 8

Input:
nums = [1, 2, 3]
k = 0
Output: 0

# Test 1: Basic example
nums = [10, 5, 2, 6]
k = 100
# Valid subarrays: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]
# Expected: 8

# Test 2: All elements < k
nums = [1, 2, 3]
k = 10
# All subarrays: [1], [2], [3], [1,2], [2,3], [1,2,3]
# Expected: 6

# Test 3: All elements > k
nums = [100, 200, 300]
k = 50
# No valid subarrays
# Expected: 0

# Test 4: Edge case — product hits exactly k
nums = [10, 10]
k = 100
# [10], [10], [10,10] → product = 100 → not valid
# Expected: 2

# Test 5: Single element equals k
nums = [5]
k = 5
# 5 is not < 5
# Expected: 0

# Test 6: Single element less than k
nums = [4]
k = 5
# Valid
# Expected: 1

# Test 7: Empty array
nums = []
k = 10
# Expected: 0

# Test 8: k = 0 (corner case)
nums = [1, 2, 3]
k = 0
# Nothing is < 0
# Expected: 0

# Test 9: k = 1 (only elements with product 0 < 1 count)
nums = [1, 2, 0, 3]
k = 1
# Only [0] is valid
# Expected: 1

# Test 10: Long array with small elements and large k
nums = [1] * 10000
k = 2
# All subarrays are valid
# Total subarrays = n * (n + 1) / 2 = 10000 * 10001 / 2
# Expected: 50,005,000

# Test 11: Alternating small and large numbers
nums = [1, 1000, 1, 1000, 1]
k = 100
# Only subarrays around 1s are valid
# Expected: 3 ([1], [1], [1])
'''

def find_no_of_substrings(input_val, max_allowed):
    if not max_allowed or (max_allowed == 1 and 0 not in input_val):
        return 0
    if max_allowed == 1:
        count_of_zeros = input_val.count(0)
        count_of_zeros += len(input_val)
        return count_of_zeros
    total_count = 0
    pivot_ptr = 0
    product = 1
    for current_ptr in range(len(input_val)):
        print(f"current position::: {current_ptr}")
        product = product * input_val[current_ptr]
        print(f"Product::: {product}")
        while product >= max_allowed:
            '''
            To move the pointer from left to right
            and remove that element from total product
            '''
            print(input_val[pivot_ptr:current_ptr+1])
            print(f"current pivot position::: {pivot_ptr}")
            product = product//input_val[pivot_ptr]
            pivot_ptr += 1
            print(f"Product::: {product}")
            print(f"current pivot position::: {pivot_ptr}")
            print("====" * 10)
        print(f"values considered for this cycle::: {input_val[pivot_ptr:current_ptr+1]}")
        print(f"count for this cycle::: {current_ptr - pivot_ptr + 1}")
        total_count += current_ptr - pivot_ptr + 1
        print("----"*10)
    return total_count



nums = [1, 1000, 1, 1000, 1]
k = 100
answer = find_no_of_substrings(nums,k)
print("Total substring counted::: ",answer)