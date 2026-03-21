# 460. LFU Cache (Hard) - LeetCode
# Design a data structure for a Least Frequently Used (LFU) cache.
#
# LFUCache(int capacity) - Initialize with given capacity.
# int get(key)           - Return value if key exists, else -1.
# void put(key, value)   - Insert/update key. When over capacity, evict the
#                          least frequently used key. On freq tie, evict the
#                          least recently used among them.
# Both get and put must run in O(1) average time complexity.
#
# Example:
#   LFUCache(2)
#   put(1,1) → cnt(1)=1
#   put(2,2) → cnt(1)=1, cnt(2)=1
#   get(1)   → 1,  cnt(1)=2
#   put(3,3) → evicts key 2 (min freq=1, LRU among ties)
#   get(2)   → -1


# ─────────────────────────────────────────────────────────────
# Solution 1: HashMap + Custom Doubly Linked List  ·  O(1) get & put
# ─────────────────────────────────────────────────────────────
# Three maps:
#   valMap   : key → value
#   countMap : key → frequency
#   listMap  : freq → DoublyLinkedList (ordered LRU→MRU by recency)
#
# lfuCnt tracks the current minimum frequency so eviction is O(1).
# On every access, a key moves from listMap[freq] → listMap[freq+1].
# When listMap[lfuCnt] empties and the access was not an insertion,
# lfuCnt increments by 1. On insertion lfuCnt always resets to 1.

from collections import defaultdict


class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    """Doubly linked list with a val→node map for O(1) removal anywhere."""

    def __init__(self):
        self.left = ListNode(0)    # dummy head (LRU end)
        self.right = ListNode(0)   # dummy tail (MRU end)
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {}              # val -> node  (for O(1) random removal)

    def length(self):
        return len(self.map)

    def pushRight(self, val):
        """Insert val at MRU end (just before dummy tail)."""
        node = ListNode(val)
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.map[val] = node

    def pop(self, val):
        """Remove a specific val from anywhere in O(1)."""
        if val in self.map:
            node = self.map[val]
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev
            del self.map[val]

    def popLeft(self):
        """Remove and return the LRU val (leftmost real node)."""
        if self.left.next == self.right:
            return None                # list is empty
        val = self.left.next.val
        self.pop(val)
        return val

    def update(self, val):
        """Move val to MRU end (used when recency changes but freq stays)."""
        self.pop(val)
        self.pushRight(val)


class LFUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.lfuCnt = 0              # current minimum frequency in the cache

        self.valMap = {}                          # key → value
        self.countMap = defaultdict(int)          # key → frequency
        self.listMap = defaultdict(LinkedList)    # freq → LinkedList of keys

    def counter(self, key):
        """Increment key's frequency and move it to the next freq bucket."""
        cnt = self.countMap[key]
        self.countMap[key] += 1

        # move key from its old freq list to freq+1 list (at MRU end)
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].pushRight(key)

        # if the old min-freq bucket is now empty and we didn't insert
        # a brand-new key, the global minimum moves up by 1
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1

    def get(self, key):
        if key not in self.valMap:
            return -1

        self.counter(key)            # accessing raises frequency
        return self.valMap[key]

    def put(self, key, value):
        if self.cap == 0:
            return

        if key not in self.valMap and len(self.valMap) == self.cap:
            # cache full: evict the LRU key from the min-freq bucket
            lru = self.listMap[self.lfuCnt].popLeft()
            del self.valMap[lru]
            del self.countMap[lru]

        self.valMap[key] = value
        self.counter(key)            # new key gets freq 1; existing key bumps
        # after insertion lfuCnt can only be 1 (new key always has freq 1
        # after counter()) — but counter() may have bumped it for updates,
        # so clamp it down to the key's actual new frequency
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])


# ─────────────────────────────────────────────────────────────
# Solution 2: HashMap + OrderedDict  ·  O(1) get & put
# ─────────────────────────────────────────────────────────────
# Same three-map idea but uses Python's OrderedDict (insertion-ordered)
# as the per-frequency bucket instead of a custom linked list.
#
# OrderedDict gives O(1) append (new key → MRU), O(1) popitem(last=False)
# (evict LRU), and O(1) move_to_end (promote to MRU on access).
# This is cleaner to write; the custom-list version avoids the overhead
# of Python's dict re-hashing on every move.
#
# Key insight for put on an existing key: just call self.get() to reuse
# the frequency-update logic, then overwrite the value afterward.

from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.minFreq = 0                              # current minimum frequency
        self.keyToVal = {}                            # key → value
        self.keyToFreq = {}                           # key → frequency
        self.freqToKeys = defaultdict(OrderedDict)    # freq → {key: None} ordered LRU→MRU

    def get(self, key: int) -> int:
        if key not in self.keyToVal:
            return -1

        freq = self.keyToFreq[key]

        # remove key from its current frequency bucket
        del self.freqToKeys[freq][key]
        if not self.freqToKeys[freq]:          # bucket now empty
            del self.freqToKeys[freq]
            if self.minFreq == freq:           # global min must move up
                self.minFreq += 1

        # promote key to freq+1 bucket at MRU end
        self.keyToFreq[key] += 1
        self.freqToKeys[freq + 1][key] = None

        return self.keyToVal[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.keyToVal:
            # update value and bump frequency by reusing get()'s logic
            self.keyToVal[key] = value
            self.get(key)                      # get() handles freq promotion
            return

        if len(self.keyToVal) == self.cap:
            # evict LRU key from the lowest-frequency bucket
            lru_key, _ = self.freqToKeys[self.minFreq].popitem(last=False)
            del self.keyToVal[lru_key]
            del self.keyToFreq[lru_key]

        # insert brand-new key with frequency 1
        self.keyToVal[key] = value
        self.keyToFreq[key] = 1
        self.freqToKeys[1][key] = None
        self.minFreq = 1                       # new key always has the lowest freq


# ─────────────────────────────────────────────────────────────
# Driver
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    print(lfu.get(1))   # 1      cnt(1)=2, cnt(2)=1
    lfu.put(3, 3)       # evicts 2 (min freq=1, LRU)
    print(lfu.get(2))   # -1
    print(lfu.get(3))   # 3      cnt(3)=2, cnt(1)=2
    lfu.put(4, 4)       # evicts 1 (tie at freq=2, 1 is LRU)
    print(lfu.get(1))   # -1
    print(lfu.get(3))   # 3
    print(lfu.get(4))   # 4
