'''
HARD

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''

class Solution:
    '''
    Runtime
7
ms
Beats
16.66%

Memory
18.06
MB
Beats
58.68%

    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_num = sorted(nums1 + nums2)
        print(final_num)
        if len(final_num)%2 == 0:
            median = float(sum(final_num[int(len(final_num)/2)-1:int(len(final_num)/2+1)])/2)
        else:
            median = float(final_num[int(len(final_num)/2)])
        print(median)
        return median