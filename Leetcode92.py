# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pre = tail = fake_head = ListNode()
        fake_head.next = head

        while left > 1:
            pre = pre.next
            left -=1
        
        while right >= 0:
            tail = tail.next
            right -=1

        nxt = tail
        cur: ListNode = pre.next
        while pre.next is not nxt:
            pre.next = cur.next
            cur.next = tail
            tail = cur
            cur = pre.next

        pre.next = tail

        return fake_head.next
