# 146. LRU Cache (Medium) - LeetCode
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# LRUCache(int capacity) - Initialize with positive size capacity.
# int get(int key)       - Return value if key exists, else -1.
# void put(int key, val) - Insert/update key. If over capacity, evict least recently used key.
# Both get and put must run in O(1) average time complexity.
#
# Example:
#   LRUCache(2)
#   put(1,1) → cache: {1=1}
#   put(2,2) → cache: {1=1, 2=2}
#   get(1)   → 1
#   put(3,3) → evicts 2, cache: {1=1, 3=3}
#   get(2)   → -1
#   put(4,4) → evicts 1, cache: {4=4, 3=3}
#   get(1)   → -1
#   get(3)   → 3
#   get(4)   → 4


# ─────────────────────────────────────────────────────────────
# Approach: HashMap + Doubly Linked List  ·  O(1) get & put
# ─────────────────────────────────────────────────────────────
# - HashMap (key → node) gives O(1) lookup.
# - Doubly linked list tracks usage order:
#     LEFT dummy  ←→  [LRU ... MRU]  ←→  RIGHT dummy
# - On get/put: move accessed node to right (MRU end).
# - On eviction: remove node from left (LRU end).

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}          # key -> node

        # dummy sentinel nodes
        self.left = Node(0, 0)   # LRU end
        self.right = Node(0, 0)  # MRU end

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        # insert at MRU end (just left of right sentinel)
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)    # mark as most recently used
            return node.val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.next     # least recently used
            self.remove(lru)
            del self.cache[lru.key]


# ─────────────────────────────────────────────────────────────
# Driver
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))   # 1
    lru.put(3, 3)
    print(lru.get(2))   # -1
    lru.put(4, 4)
    print(lru.get(1))   # -1
    print(lru.get(3))   # 3
    print(lru.get(4))   # 4
