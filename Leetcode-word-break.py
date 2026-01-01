'''
Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''


class Solution:
    '''
    Runtime 30 ms Beats 6.26%
    Memory 17.72 MB Beats 72.38%
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        temp_list = [False] * (len(s)+1)
        temp_list[0] = True
        for i in range(1,len(s)+1):
            for j in range(i):
                print(s[j:i])
                if temp_list[j] and s[j:i] in wordDict:
                    temp_list[i] = True
                    print(temp_list)
                    break
        return temp_list[-1]