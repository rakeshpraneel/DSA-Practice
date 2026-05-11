'''
Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
'''


class Solution:
    '''
    Runtime
7
ms
Beats
72.06%

Memory
23.26
MB
Beats
15.92%
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        # print(intervals)

        merged = [intervals[0]]
        # print(merged)
        # print(merged[-1])

        for start, end in intervals[1:]:
            if merged[-1][-1] >= start:
                merged[-1][-1] = end if end > merged[-1][-1] else merged[-1][-1]
            else:
                merged.append([start, end])
        # print(merged)
        return merged


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[1])
        print(intervals)
        dp = [False] * (intervals[-1][1] + 1)
        print(dp)
        final = []
        for i in intervals:
            for j in range(i[0], i[1] + 1):
                dp[j] = True
        print(dp)
        first = True
        start_index = 1
        for i in range(len(dp)):
            if dp[i] and first:
                print(f"First true found....value:{i}")
                start_index = i
                first = False
            elif not dp[i] and not first:
                print(f"First false found after starting index....value:{i - 1}")
                final.append([start_index, i - 1])
                first = True
            elif i == len(dp) - 1 and dp[i]:
                print(f"Last index after starting index....value:{i}")
                final.append([start_index, i])

        print(final)
        return final





