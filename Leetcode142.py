# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        
        if fast is None or fast.next is None:
            return None
        
        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        print(type(fast))
        return fast