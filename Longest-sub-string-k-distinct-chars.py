'''
Longest Substring with At Most K Distinct Characters

Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters.

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece"

Input: s = "aa", k = 1
Output: 2
Explanation: "aa" has exactly one distinct character

s = "aaaaa"
k = 1
# All characters are the same, valid
# Expected Output: 5

s = "abcdef"
k = 3
# Possible longest: "abc", "bcd", "cde", "def"
# Expected Output: 3

s = "abcdef"
k = 6
# Entire string is valid
# Expected Output: 6

s = "abc"
k = 0
# No valid substring can have 0 distinct characters
# Expected Output: 0

s = ""
k = 2
# Nothing to process
# Expected Output: 0

s = "aabacbebebe"
k = 3
# Longest substring: "cbebebe"
# Expected Output: 7

s = "aaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccdddddd"
k = 2
# The longest valid substring would be max chunk of any 2 characters
# Expected Output: Length of "bbbb...ccccc" or "aaaaa...bbbb" (depending on distribution)
# Rough Expected Output: ≥ 30

s = "abc" * 10000  # Length = 30000
k = 2
# Sliding window should only ever keep 2 distinct chars
# Expected Output: 2

s = "abaccc"
k = 2
# Longest = "accc"
# Expected Output: 4
'''

'''
eceba here k = 2
'''
import time
from collections import defaultdict
def find_longest_substring(input_val, length):
    tracker = defaultdict(int)
    max_len = 0
    pivot_ptr = 0
    for current_ptr in range(len(input_val)):
        tracker[input_val[current_ptr]] += 1
        while len(tracker) > k:
            print(tracker)
            print(len(tracker))
            tracker[input_val[pivot_ptr]] -= 1
            if tracker[input_val[pivot_ptr]] == 0:
                del tracker[input_val[pivot_ptr]]
            pivot_ptr += 1
        max_len = max(max_len,current_ptr-pivot_ptr+1)
    return max_len

def find_longest_substring_conventional(input_val, length):
    temp_list = []
    max_length = 0
    for i in range(len(input_val)):
        temp_list.clear()
        for j in range(i,len(input_val)):
            temp_list.append(input_val[j])
            print(temp_list)
            if len(set(temp_list)) > length:
                print(f"more than {length} distinct found::: {temp_list}")
                max_length =  len(temp_list)-1 if len(temp_list) - 1 > max_length else max_length
                temp_list.clear()
                print(f"Max length::: {max_length}")
            elif j == len(input_val)-1:
                print(f"reached end of list without exceeding k::: {temp_list}")
                max_length = len(temp_list) if len(temp_list) > max_length else max_length
    max_length = max_length if max_length != 0 or length == 0 else len(input_val)
    return max_length
s = "aabcdefff"
k = 3
start = time.time()
answer = find_longest_substring_conventional(s,k)
print(answer)
end = time.time()
print(end-start)
print("*****"*10)
start = time.time()
answer = find_longest_substring(s,k)
print(answer)
end = time.time()
print(end-start)
print("*****"*10)