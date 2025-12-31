'''
Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
'''


class Solution:
    '''
    Memory 17.44 MB Beats 89.36%
    Runtime 8348 ms Beats 5.00%
    '''
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        answer = ""
        for i in range(0,len(s)):
            for j in range(len(s)-1,i,-1):
                # print(s[i:j+1])
                # print("---"*5)
                comp_val = s[i:j+1]
                if comp_val == comp_val[::-1]:
                    answer = s[i:j+1] if len(answer) < j-i+1 else answer
                    # print(answer)
                    j = 0
                    # print("***"*3)
            # print("internal loop completed")
        return answer if answer else s[0]