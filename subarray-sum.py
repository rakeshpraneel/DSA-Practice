'''
Input: nums = [1, 2, 3], k = 3
Output: 2
Explanation:
- Subarrays: [1, 2], [3]

nums = [1, 1, 1]
k = 2
# Explanation: [1,1] at positions (0,1), (1,2)
# Expected Output: 2

nums = [1, -1, 0]
k = 0
# Explanation: [1,-1], [0], [1,-1,0]
# Expected Output: 3

nums = [3, 4, -7, 1, 3, 3, 1, -4]
k = 7
# Explanation: [3, 4], [1, 3, 3], [3, 4, -7, 1, 3, 3], [3, 3, 1]
# Expected Output: 4
=====================================================================
nums = [1, 2, -3] * 10000  # length = 30,000
k = 0

# Explanation:
# Each full pattern [1, 2, -3] adds to 0
# So, every combination of multiple [1,2,-3]s contributes valid subarrays

# Output: Large number (you'll observe the count)
'''
from collections import defaultdict
import time

# Hashing and Reverse Iteration logic
'''
storing sum for each and every position in a dict on the go
and parallely checking if the previous sum as met the expected
k value.

worst case scenario time taken::: 0.005002737045288086
'''
def calculate_subarray(input_val, total):
    tracker = defaultdict(int)
    tracker[0] = 1
    local_total = 0
    counter = 0
    for val in input_val:
        local_total += val
        if local_total - total in tracker:
            counter += tracker[local_total-total]
        tracker[local_total] += 1
    return counter

# Conventional loop
'''
picking ith element and summing it with i+1...nth
and count if it equals to k and repeat this till
nth element.
worst case scenario time taken::: 22.52490758895874
'''
def calculate_subarray_old(input_val, total):
    counter = 0
    for i in range(len(input_val)):
        local_total = 0
        for j in range(i,len(input_val)):
            local_total+=input_val[j]
            if local_total == total:
                counter+=1
    return counter

nums = [1, 2, -3] * 10000
k = 0
start = time.time()
answer = calculate_subarray(nums, k)
print(answer)
end = time.time()
print(end-start)
print("*****"*10)
start = time.time()
answer = calculate_subarray_old(nums, k)
print(answer)
end = time.time()
print(end-start)
print("*****"*10)