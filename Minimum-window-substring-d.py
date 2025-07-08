'''
Difficult
Problem: Minimum Window Substring
Given two strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
If there is no such window, return an empty string "".

Input:
s = "ADOBECODEBANC"
t = "ABC"
Output: "BANC"

Input: s = "a", t = "a"
Output: "a"

Input: s = "a", t = "aa"
Output: ""
# Explanation: 'a' appears only once in `s`, but we need two.

# Test Case 4: Minimum window is at the start
s = "aaabcbc"
t = "abc"
# Expected: "aabcbc" or "abcbc" depending on path — "abcbc" is minimal → Expected: "abc"

# Test Case 5: Minimum window is at the end
s = "xyzabc"
t = "abc"
# Expected: "abc"

# Test Case 6: Whole string is the window
s = "aabc"
t = "aabc"
# Expected: "aabc"

# Test Case 7: Characters not in source
s = "hello"
t = "world"
# Expected: ""

# Test Case 8: Empty input string
s = ""
t = "abc"
# Expected: ""

# Test Case 9: Empty target
s = "abc"
t = ""
# Expected: ""

# Test Case 10: Long string with match
s = "a" * 10000 + "b" + "c" * 10000
t = "abc"
# Expected: "ab"

# Test Case 11: Long string, no match
s = "a" * 100000
t = "abc"
# Expected: ""

# Test Case 12: Unicode characters
s = "αβγδεζηθικλμνξοπρστυφχψω"
t = "σψω"
# Expected: "στυφχψω"
'''
from time_calculator import timer_function
from collections import defaultdict, Counter

@timer_function
def find_min_substring(input_val, sub_string):
    tracker = defaultdict(int)
    if input_val == sub_string:
        return input_val
    current_shortest_substring = input_val
    pivot_ptr = 0
    matching_chars_found = 0
    sub_string_count = Counter(sub_string)
    matching_chars_needed = len(sub_string_count)
    print(sub_string_count)
    for current_ptr in range(len(input_val)):
        print(f"current pointer::: {current_ptr}")
        print(f"current matching chars::: {matching_chars_found}")
        val = input_val[current_ptr]
        tracker[input_val[current_ptr]] += 1
        print(tracker)
        if val in sub_string_count and tracker[val] == sub_string_count[val]:
            matching_chars_found += 1
        while matching_chars_needed == matching_chars_found and matching_chars_needed:
            print(f"pivot pointer::: {pivot_ptr}")
            print("Required values matched")
            print(tracker)
            current_shortest_substring = input_val[pivot_ptr:current_ptr+1] if len(input_val[pivot_ptr:current_ptr+1]) < len(current_shortest_substring) else current_shortest_substring
            tracker[input_val[pivot_ptr]] -= 1
            print("After decreasing pivot pointer count")
            print(tracker)
            if input_val[pivot_ptr] in sub_string_count and tracker[input_val[pivot_ptr]] < sub_string_count[input_val[pivot_ptr]]:
                matching_chars_found -= 1
            pivot_ptr += 1

    return "" if current_shortest_substring == sub_string else current_shortest_substring


s = "αβγδεζηθικλμνξοπρστυφχψω"
t = "σψω"
answer = find_min_substring(s,t)

print(f"answer:: {answer}")