'''
Problem: Longest Substring with Character Replacement
You are given a string s and an integer k.
Return the length of the longest substring that can be obtained by replacing at most k characters in the string so that all characters in the substring are the same.

Input:
s = "ABAB"
k = 2
Output: 4
Explanation: Replace both 'A's or both 'B's to make all same → "AAAA" or "BBBB"

# Test 2: Small replacement limit
s = "AABABBA"
k = 1
# Longest valid window → "ABBB"
# Expected: 4

# Test 3: No replacement needed
s = "AAAA"
k = 2
# Already all same
# Expected: 4

# Test 4: Replace entire string
s = "ABCDE"
k = 4
# Replace any 4 → turn into "AAAAA"
# Expected: 5

# Test 5: Alternating pattern
s = "ABABABAB"
k = 1
# Best window is "ABA" or "BAB" → change one to get "AAA" or "BBB"
# Expected: 3

# Test 6: Empty string
s = ""
k = 2
# Expected: 0

# Test 7: All different, not enough k
s = "ABCDE"
k = 2
# Max 3-length window like "ABC" → replace 2
# Expected: 3

# Test 8: Not enough replacements
s = "AABBBCCDDDD"
k = 0
# Only solid blocks count
# Expected: 4 (the DDDD)

# Test 9: Large string, low k
s = "A" * 10000 + "B" * 10000
k = 1
# Can't convert entire section, max = "A"*10001 or "B"*10001
# Expected: 10001

# Test 10: Long alternating pattern
s = "AB" * 5000
k = 5000
# Best: Replace all B's to get "AAAA...A" (or vice versa)
# Expected: 10000
'''
from collections import defaultdict
def find_longest_substring(input_val, max_allowed_freq):
    '''
    Storing frequency of each character using current pointer by iterating
    pivot pointer is used to slide the window from left.
    current window = length of currently considered string.
    similarly maximum frequency of currently considered chars are tracked
    and when the difference between current window and this frequency exceeds than max allowed freq
    then pivot positioned element frequency is decremented from the tracker and pivot is incremented

    (ie) subracting maximum number of repeated characters in the considered string from current window
    will give you the count of remaining characters there by we can find whether it is within max allowed freq
    so that we can replace those values and achieve the result.

    (eg) Input string: AAAABBHG; max allowed freq: 2
    in this, while reading value from 4th position, the current considered string will be AAAAB
    tracker will have A:4 and B:1; size of current window: current_position - pivot + 1 = 4-0+1 = 5
    and maximum frequency of currently considered chars: 4 (Max of A:4 and B:1)

    Now to find the count of less repeated chars, we need to subtract maximum frequency of currently considered chars
    from current window which will be 1 and this is less than max allowed freq: 2 so we can extend our limit

    Now in next iteration, the current considered string will be AAAABB; current position: 5
    tracker will have A:4 and B:2; size of current window: current_position - pivot + 1 = 5-0+1 = 6
    and maximum frequency of currently considered chars: 4 (Max of A:4 and B:2)

    Now the difference became 2 which we can fill up using max allowed freq but still it's not higher than that
    so we can go one more iteration.

    Now in next iteration, the current considered string will be AAAABBH; current position: 6
    tracker will have A:4 and B:2 and H:1; size of current window: current_position - pivot + 1 = 6-0+1 = 7
    but maximum frequency of currently considered chars will be still 4 (Max of A:4 and B:2 and H:1)

    Now the difference became 3 which is higher than max allowed freq: 2. So we will decrement the pivot positioned
    value from tracker and increment the pivot position (thereby we are moving the pointer towards right)
    tracker= A:3 and B:2 and H:1; Pivot position: 1

    this makes the current window size to 6-1+1=6 which will be considered as max_possible length of substring.

    This logic repeats till the last character of input string.
    '''
    tracker = defaultdict(int)
    pivot_ptr = 0
    max_freq = 0
    max_substring = 0
    print(f"maximum allowed freq::: {max_allowed_freq}")
    for current_ptr in range(len(input_val)):
        current_char = input_val[current_ptr]
        tracker[input_val[current_ptr]] += 1
        window_size = current_ptr - pivot_ptr + 1
        max_freq = max(max_freq,tracker[current_char])
        print(f"string under consideration::: {input_val[pivot_ptr:current_ptr + 1]}")
        print(f"windows size::: {window_size}")
        print(f"tracker::: {tracker}")
        print(f"maximum freq::: {max_freq}")

        if window_size - max_freq > max_allowed_freq:
            tracker[input_val[pivot_ptr]] -= 1
            pivot_ptr += 1
        print(f"Pivot pointer::: {pivot_ptr}")
        max_substring = max(max_substring, current_ptr - pivot_ptr + 1)
        print(f"maximum substring length::: {max_substring}")
    return max_substring

s = "AB" * 5000
k = 5000
answer = find_longest_substring(s,k)
print(f"Final answer::: {answer}")