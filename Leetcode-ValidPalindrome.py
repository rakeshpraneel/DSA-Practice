
'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''


class Solution:
    '''
    Runtime
3
ms
Beats
98.98%

Memory
20.61
MB
Beats
24.30%
    '''
    def isPalindrome(self, s: str) -> bool:
        import re

        s = re.sub("[^a-zA-Z0-9]","",s).lower()
        print(s)
        if s == s[::-1]:
            return True
        return False