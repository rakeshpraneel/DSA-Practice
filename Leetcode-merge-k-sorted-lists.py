'''
Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
'''

import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Runtime 11ms Beats 60.67%
    Memory 19.70 MB Beats 87.67%

    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = []
        for l in lists:
            current_node = l
            while current_node is not None:
                heapq.heappush(queue,current_node.val)
                current_node = current_node.next
        if queue:
            head = ListNode()
            current_node = head
            while queue:
                current_node.val = heapq.heappop(queue)
                if len(queue) > 0:
                    current_node.next = ListNode()
                    current_node = current_node.next
            # print(head)
            return head
        return None
