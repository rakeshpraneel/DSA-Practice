'''
Rotate List
Given the head of a linked list, rotate the list to the right by k places.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Runtime 0ms Beats 100.00%
    Memory 19.24MB Beats 90.65%

    '''
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail = head
        length = 1
        if not head:
            return head
        while (tail.next):
            tail = tail.next
            length += 1
        print(length)

        k = k % length
        print(k)

        tail.next = head
        new_tail = head
        # print(tail)
        for i in range(length-k-1):
            new_tail = new_tail.next
        # print(new_tail)
        new_head = new_tail.next
        new_tail.next = None
        # print(new_head)
        # print(new_tail)
        # print(tail)

        return new_head