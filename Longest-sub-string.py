'''
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
s = "aaaaaaaaaaaaaaaaaa"
s = "pwwkew"
s = "abc!@#abc!@#"
s = "a" * 10000 + "b" * 10000 + "c" * 10000
s = ""
s = "🙂🙃🙂🙃🙂"
s = "abcdabcdeabcdef"
# Expected output: 6 ("abcdef")
s = "a" * 99999999 + "b" * 10000 + "c" * 10000
s = "abcde" * 2000
s = "".join([chr(97 + (i % 26)) for i in range(10000)])
'''
import time


def get_string_dict(input_val):
    comparing_list = {}
    start = 0
    max_len = 0
    for i in range(len(input_val)):
        if input_val[i] in comparing_list and comparing_list[input_val[i]] >= start:
            start = comparing_list[input_val[i]]+1
        comparing_list[input_val[i]] = i
        max_len = max(max_len,i - start + 1)
    return max_len

def get_string(input_val):
    max_len = 0
    comparing_list = []
    position = 0
    for i in input_val:
        if i not in comparing_list:
            comparing_list.append(i)
            max_len = len(comparing_list) if len(comparing_list) > max_len else max_len
        else:
            comparing_list.clear()
            comparing_list.append(i)
            if len(input_val) - position < max_len:
                break
        position+=1
    return max_len

s = "".join([chr(97 + (i % 26)) for i in range(1_000_000)])
# print(s)
start = time.time()
answer = get_string(s)
end = time.time()
print(answer)
print(end-start)
print("*****"*10)
start = time.time()
answer = get_string_dict(s)
end = time.time()
print(answer)
print(end-start)