'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''

class Solution:
    '''
    Time Complexity: 4 ms Beats 33.50%
    Space Complexity: 18.32 MB Beats 18.89%
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        answer = sorted(nums1 + nums2)
        print(answer)
        if (len(nums1)+len(nums2))%2 == 0:
            print(int(((len(nums1)+len(nums2))/2)-1))
            print(int((len(nums1)+len(nums2))/2))
            return sum(answer[int(((len(nums1)+len(nums2))/2)-1):int((len(nums1)+len(nums2))/2)+1])/2
        else:
            print(int((len(nums1)+len(nums2)+1)/2))
            return answer[int((len(nums1)+len(nums2)+1)/2)-1]