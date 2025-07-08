'''
Palindrome Pairs
LeetCode 336 – Hard

You are given a list of unique words, return all the pairs of distinct indices (i, j)
in the list such that the concatenation words[i] + words[j] is a palindrome.

Input: words = ["bat", "tab", "cat"]
Output: [[0,1],[1,0]]

# Explanation:
# "bat" + "tab" = "battab" (palindrome)
# "tab" + "bat" = "tabbat" (palindrome)

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]

# Explanation:
# "abcd" + "dcba" = palindrome
# "s" + "lls" = "slls"
# "lls" + "sssll" = "llssssll"

words = ["", "a"]
# Expected: [[0, 1], [1, 0]]

words = ["a", "aa", "aaa"]
# Expected: [[0, 1], [1, 0], [0, 2], [2, 0], [1, 2], [2, 1]]

words = ["abc", "def", "ghi"]
# Expected: []

words = ["abc", "cba", "bca"]
# Expected: [[0, 1], [1, 0]]

import random, string

words = [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(1000)]
# Expect: likely [], unless accidental palindromes
'''

import time_calculator
@time_calculator.timer_function
def find_palindrome_pair(input_val):
    hash_map_indexing = {word: index for index, word in enumerate(input_val)}
    print(hash_map_indexing)
    list_of_indices = set()
    for i in range(len(input_val)):
        print(input_val[i][::-1])
        if input_val[i][::-1] in hash_map_indexing and i != hash_map_indexing.get(input_val[i][::-1]):
            list_of_indices.add((i,hash_map_indexing.get(input_val[i][::-1])))
        for j in range(len(input_val[i])):
            current_word = input_val[i][j:]
            current_word_reverse = input_val[i][:j]
            # print(f"current word iteration>>> {current_word}")
            # print(f"current word reverse iteration>>> {current_word_reverse}")
            print(f"i value::: {i}")
            print(f"current word::: {current_word} & reversed::: {current_word[::-1]}")
            print(f"reverse iterated current word::: {current_word_reverse} & reversed::: {current_word_reverse[::-1]}")
            if current_word == current_word[::-1]:
                suffix_reversed = current_word_reverse[::-1]
                if suffix_reversed in hash_map_indexing and i != hash_map_indexing.get(suffix_reversed):
                    print(f"current word {current_word} is palindrome and it is present in hash dictionary {hash_map_indexing}")
                    print(hash_map_indexing.get(suffix_reversed))
                    list_of_indices.add((hash_map_indexing.get(suffix_reversed),i))
            if current_word_reverse == current_word_reverse[::-1]:
                prefix_reversed = current_word[::-1]
                if prefix_reversed in hash_map_indexing and i != hash_map_indexing.get(prefix_reversed):
                    print(f"current word reverse iteration {prefix_reversed} is palindrome and it is present in hash dictionary {hash_map_indexing}")
                    print(hash_map_indexing.get(prefix_reversed))
                    list_of_indices.add((i,hash_map_indexing.get(prefix_reversed)))
        print("----"*10)

    return (list_of_indices)


def cleanup(output_list):
    return list(set(output_list))

import random, string

words = [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(1000)]
answer = find_palindrome_pair(words)
# answer = cleanup(answer)
print(answer)