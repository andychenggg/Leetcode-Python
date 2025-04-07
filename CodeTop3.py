# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Codetop3, Leetcode25.
https://leetcode.cn/problems/reverse-nodes-in-k-group/submissions/619975602/
'''
class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pre: ListNode = ListNode()
        cur = pre
        pre.next = head
        while True:
            res: ListNode = self.reverseK(cur, k)
            if res is None:
                return pre.next
            cur = res

    def reverseK(self, pre: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur: ListNode = pre.next
        res: ListNode = pre.next
        tail: ListNode = pre.next

        for i in range(k):
            if tail is None:
                return None
            tail = tail.next
        
        for i in range(k):
            pre.next = cur.next
            cur.next = tail
            tail = cur
            cur = pre.next
        pre.next = tail
        return res

