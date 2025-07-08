'''
Level 9 Problem: Maximum Points from Cards
LeetCode 1423 – Hard Level

You are given an integer array cardPoints and an integer k. In one move, you can take one card from the beginning or the end of the array. You have to pick exactly k cards.

Return the maximum score you can obtain by picking exactly k cards from either end.

cardPoints = [1,2,3,4,5,6,1]
k = 3

Output: 12
>> Pick cards 6, 1, and 5 (from end and start) → 6 + 1 + 5 = 12

Test cases:
cardPoints = [5, 5, 5, 5, 5]
k = 3
# Expected: 15

cardPoints = [1, 2, 3, 4]
k = 4
# Expected: 10

cardPoints = [9, 7, 7, 9, 7, 7, 9]
k = 7
# Expected: sum(all) = 55

cardPoints = [100, 40, 17, 9, 73, 75]
k = 3
# Try: [100, 40, 17] → 157
# Try: [100, 40] + [75] → 215
# Try: [100] + [75, 73] → 248 ✅
# Try: [75, 73, 9] → 157
# Expected: 248

cardPoints = [1, 1000, 1]
k = 1
# Expected: 1

cardPoints = [1] * 100000
k = 99999
# Expected: 99999
'''

def find_max_points(input_val, max_iteration):
    max_ = sum(input_val[:max_iteration])
    print(f"Initial max::: {max_}")
    dynamic_max = max_
    if max_iteration == len(input_val):
        return max_
    for i in range(k):
        print(f"removing {k-i-1}th element {input_val[k-i-1]} from list and adding {len(input_val)-1-i}th element {input_val[len(input_val)-1-i]}")
        dynamic_max = dynamic_max - input_val[k-i-1] + input_val[len(input_val)-1-i]
        print(f"dynamic max::: {dynamic_max}")
        max_ = max(dynamic_max,max_)
    return max_


cardPoints = [1] * 100000
k = 99999
answer = find_max_points(cardPoints, k)
print(answer)