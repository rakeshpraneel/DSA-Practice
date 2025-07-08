'''
Longest Substring with At Most K Repeating Characters (with frequency limit)
You are given a string s and two integers k and max_repeats.
Return the length of the longest substring where:

The substring contains at most k distinct characters

No character appears more than max_repeats times

Input: s = "aaabbcc", k = 2, max_repeats = 2
Output: 4
Explanation: Substring = "aabb" or "bbcc"

Input: s = "aabcdefff", k = 3, max_repeats = 2
Output: 5
Explanation: "aabcd" is valid

s = "aaaaa"
k = 1
max_repeats = 3
# Explanation: Only 3 'a's allowed → max length = 3
# Expected: 3

s = "abcde"
k = 2
max_repeats = 1
# Explanation: Max substring with 2 distinct and each at most once → "ab", "bc", etc.
# Expected: 2

s = "aabbccdd"
k = 3
max_repeats = 1
# Explanation: Each character can only appear once → valid substrings: "a", "ab", "abc", etc.
# Expected: 3

s = "ababcc"
k = 3
max_repeats = 2
# All characters appear ≤ 2, only 3 distinct → whole string is valid
# Expected: 6

s = "aabbaaaccbb"
k = 2
max_repeats = 2
# Many times the window will shrink due to 3rd character or exceeding repeat
# Expected: 4 ("aabb" or "bbaa")

s = ""
k = 2
max_repeats = 2
# Expected: 0

s = "aabbaacc"
k = 1
max_repeats = 2
# Only substrings like "aa", "bb", "cc" → max = 2
# Expected: 2

s = "aaaaaaaaaa"
k = 1
max_repeats = 4
# Only 4 'a's allowed
# Expected: 4

s = "abc" * 10000  # Length = 30000
k = 2
max_repeats = 2
# Expect window to break every few characters → longest = 4
# Expected: 4
'''

from collections import defaultdict
def find_longest_substring(input_val, length, repeat):
    tracker = defaultdict(int)
    max_len = 0
    pivot_ptr = 0
    for current_ptr in range(len(input_val)):
        print(f"current pointer position::: {current_ptr}")
        tracker[input_val[current_ptr]] += 1
        while len(tracker) > length or any(values > repeat for values in tracker.values()):
            print(tracker)
            print(f"pivotal pointer position::: {pivot_ptr}")
            tracker[input_val[pivot_ptr]] -= 1
            if tracker[input_val[pivot_ptr]] == 0:
                del tracker[input_val[pivot_ptr]]
            pivot_ptr += 1
        max_len = max(max_len,current_ptr-pivot_ptr+1)
        print(f"max length::: {max_len}")
        print("-----"*10)
    return max_len

s = "abc" * 10000  # Length = 30000
k = 2
max_repeats = 2

answer = find_longest_substring(s,k ,max_repeats)
print(answer)