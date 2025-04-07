'''
CodeTop2, Leetcode146.
https://leetcode.cn/problems/lru-cache/
'''


class Node:
        def __init__(self, key: int, val: int):
            self.key: int = key
            self.val: int  = val
            self.next = None
            self.pre = None
        
        @staticmethod
        def insertBehind(node: 'Node', behindNode: 'Node') -> None:
            pre: "Node" = node
            post: "Node" = node.next
            pre.next = behindNode
            behindNode.pre = pre
            post.pre = behindNode
            behindNode.next = post
                    
        @staticmethod
        def removeNode(node: "Node") -> None:
            pre: 'Node' = node.pre
            post: 'Node' = node.next
            pre.next = post
            post.pre = pre

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cacheMap: dict = dict()
        self.head: Node = Node(0, 0)
        self.tail: Node = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            cur: Node = self.cacheMap[key]
            Node.removeNode(cur)
            Node.insertBehind(self.head, cur)
            return cur.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            cur: Node = self.cacheMap[key]
            cur.val = value
            Node.removeNode(cur)
            Node.insertBehind(self.head, cur)
        elif len(self.cacheMap) < self.capacity:
            cur: Node = Node(key, value)
            self.cacheMap[key] = cur
            Node.insertBehind(self.head, cur)
        else:
            rmNode: Node = self.tail.pre
            Node.removeNode(rmNode)
            del self.cacheMap[rmNode.key]

            cur: Node = Node(key, value)
            self.cacheMap[key] = cur
            Node.insertBehind(self.head, cur)


lRUCache: LRUCache = LRUCache(2)
lRUCache.put(1, 1); # 缓存是 {1=1}
lRUCache.put(2, 2); # 缓存是 {1=1, 2=2}
lRUCache.get(1);    # 返回 1
lRUCache.put(3, 3); # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    # 返回 -1 (未找到)
lRUCache.put(4, 4); # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    # 返回 -1 (未找到)
lRUCache.get(3);    # 返回 3
lRUCache.get(4);    # 返回 4