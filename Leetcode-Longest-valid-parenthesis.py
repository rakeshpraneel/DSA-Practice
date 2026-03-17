'''
Longest Valid Parentheses
Solved
Hard
Topics
premium lock icon
Companies
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.
'''

class Solution:
    '''
    Runtime 11 ms Beats 44.93%
    Memory 20.57MB Beats 56.42%
    '''
    def longestValidParentheses(self, s: str) -> int:
        i = 0
        max_ = 0
        count = 0
        stack = [-1]
        while (i < len(s)):
            # print(f"STack::: {stack}")
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    # print(f"max_ = {i} + {stack[-1]}")
                    if i - stack[-1] > max_:
                        max_ = i - stack[-1]
                    # print(f"max::: {max_}")
                else:
                    stack.append(i)
            i += 1
        return max_

