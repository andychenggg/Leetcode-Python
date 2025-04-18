# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode()
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                cur.next, cur, list1 = list1, list1, list1.next
            else:
                cur.next, cur, list2 = list2, list2, list2.next
        while list1 is not None:
            cur.next, cur, list1 = list1, list1, list1.next
        while list2 is not None:
            cur.next, cur, list2 = list2, list2, list2.next

        return head.next


        