# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        times = 2
        curA, curB = headA, headB
        while times > 0:
            if curA == curB:
                return curA
            if curA.next == None:
                curA = headB
                times -= 1
            else:
                curA = curA.next
            if curB.next == None:
                curB = headA
            else:
                curB = curB.next

        return None