'''
Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
'''


import itertools


class Solution:
    '''
    Runtime 0 ms Beats 100.00%
    Memory 19.31 MB Beats 42.61%
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        mapping_doc = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs"
            , '8': "tuv", '9': "wxyz"}
        result = [""]
        # for i in range(0,len(digits)-1):
        #     print(mapping_doc[digits[i]])
        #     answer = list(itertools.product(mapping_doc[digits[i]],mapping_doc[digits[i+1]]))
        #     print(answer)
        # print(mapping_doc)

        for value in digits:
            temp = []
            for results in result:
                print(f"results value::: {results}")
                for letters in mapping_doc[value]:
                    print(f"letters value::: {letters}")
                    temp.append(results + letters)
            result = temp
            print(temp)
        return result

