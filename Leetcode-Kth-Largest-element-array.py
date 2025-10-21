'''
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

import heapq
class Solution:
    '''
    Solved heapq so that we can find Kth element without sorting
    Time complexity: 99ms Beats 36.78%
    Space complexity: 28.75MB Beats 45.34%
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        K_list = []
        for num in nums:
            heapq.heappush(K_list,num)
            # print(K_list)
            if len(K_list) > k:
                heapq.heappop(K_list)
                # print("after poped")
                # print(K_list)
        return K_list[0]

class Solution:
    '''
    Time complexity: 52ms Beats 80.85%
    Space complexity: 28.88MB Beats 23.13%
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums,reverse=True)[k-1]
