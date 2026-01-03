'''
Find K Pairs with Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
'''


# Using heapq
import heapq
class Solution:
    '''
    Runtime 82 ms Beats 85.27%
    Memory 37.55 MB Beats 25.08%
    '''
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        final_list = []
        heap_list = []
        for i in range(min(k,len(nums1))):
            heapq.heappush(heap_list,(nums1[i]+nums2[0],i,0))
        while len(final_list) < k:
            sum_,i,j = heapq.heappop(heap_list)
            final_list.append([nums1[i],nums2[j]])
            if j < len(nums2)-1:
                heapq.heappush(heap_list,(nums1[i]+nums2[j+1],i,j+1))
        return final_list


#without heaq but will fail for complex test case
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        final_list = []
        max_sum = float(-inf)
        _sorted = False
        for i in nums1:
            if _sorted and max_sum < i+nums2[0]:
                    break
            for j in nums2:
                if _sorted and max_sum < i+j:
                    break
                final_list.append([i,j])
                if len(final_list) > k:
                    final_list = sorted(final_list, key=sum)[:k]
                    max_sum = sum(final_list[-1])
                    _sorted = True
        return final_list