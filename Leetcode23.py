# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # if len(lists) == 0:
        #     return None
        # self.mergeKListsDC(lists, 0, len(lists)-1)
        # return lists[0]

        return self.mergeKListsPQ(lists)
    

    '''
    Divide and Conquer
    '''
    def mergeKListsDC(self, lists: List[Optional[ListNode]], l: int, r: int):
        if l >= r:
            return
        
        mid = (l+r)//2
        self.mergeKListsDC(lists, l, mid)
        self.mergeKListsDC(lists, mid+1, r)

        cur = head = ListNode()
        n1 = lists[l]
        n2 = lists[mid+1]

        while n1 != None and n2 != None:
            if n1.val < n2.val:
                cur.next = n1
                n1 = n1.next
                cur = cur.next
            else:
                cur.next = n2
                n2 = n2.next
                cur = cur.next

        while n1 != None:
            cur.next = n1
            n1 = n1.next
            cur = cur.next

        while n2 != None:
            cur.next = n2
            n2 = n2.next
            cur = cur.next
        
        lists[l] = head.next
        
    def mergeKListsPQ(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        pq = []
        cur = res = ListNode()

        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(pq, (lists[i].val, id(lists[i]), lists[i]))

        while len(pq) != 0:
            item = heapq.heappop(pq)
            cur.next = item[2]
            cur = cur.next

            if item[2].next is not None:
                heapq.heappush(pq, (item[2].next.val, id(item[2].next), item[2].next))
            
        return res.next