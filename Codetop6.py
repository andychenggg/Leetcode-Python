from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

'''
Codetop6, Leetcode 206
https://leetcode.cn/problems/reverse-linked-list/description/
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur: Optional[ListNode] = head
        tail = None
        while cur is not None:
            temp = cur.next
            cur.next = tail
            tail = cur
            cur = temp

        return tail
