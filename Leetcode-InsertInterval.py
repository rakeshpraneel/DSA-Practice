'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
'''

class Solution:
    '''
    Runtime
0
ms
Beats
100.00%


Memory
21.31
MB
Beats
56.73%

    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals)
        merged = [intervals[0]]
        # print(intervals)
        # print(merged)
        for start,end in intervals:
            if merged[-1][-1] >= start:
                merged[-1][-1] = end if end > merged[-1][-1] else merged[-1][-1]
            else:
                merged.append([start,end])
        # print(merged)
        return merged