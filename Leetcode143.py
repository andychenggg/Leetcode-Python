# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head 
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        if slow is None:
            return head
        
        head1 = head
        head2 = self.reverse(slow.next)
        slow.next = None
        while head1 is not None and head2 is not None:
            tmp = head1.next
            head1.next = head2
            head1 = tmp

            tmp = head2.next
            head2.next = head1
            head2 = tmp
        return head


    def reverse(self, head: ListNode) -> None:
        tail = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = tail
            tail = cur
            cur = temp
        return tail
        
        