'''
Sort List

Given the head of a linked list, return the list after sorting it in ascending order.
Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    '''
    Runtime 95 ms Beats 82.27%
    Memory 32.70 MB Beats 71.44%
    '''
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        sort_l = []
        final_list = []
        while current_node is not None:
            heapq.heappush(sort_l ,current_node.val)
            print(current_node.val)
            current_node = current_node.next
        current_node = head
        while sort_l:
            current_node.val = heapq.heappop(sort_l)
            current_node = current_node.next
        return head
