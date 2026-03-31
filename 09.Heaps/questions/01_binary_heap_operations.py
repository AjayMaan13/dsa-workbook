"""
============================================================
PROBLEM: Binary Min-Heap — Full Implementation
Source  : TakeUForward
============================================================

Implement a Min Binary Heap that supports the following operations:

    insert(x)        — Insert a new key x into the heap.
                       Elements are inserted at the end and bubbled up
                       to maintain the min-heap property.
                       Time: O(log N)

    heapify(i)       — Fix a violation of the min-heap property at
                       index i, assuming both subtrees are valid heaps.
                       Find the smallest among node, left child, and
                       right child; swap if needed and recurse down.
                       Time: O(log N)

    get_min()        — Return the minimum element (the root, arr[0]).
                       Time: O(1)

    extract_min()    — Remove and return the minimum element.
                       Move the last element to the root, decrease size
                       by 1, then call heapify(0) to restore order.
                       Time: O(log N)

    decrease_key(i, val)
                     — Update the value at index i to val (val must be
                       ≤ current value). Bubble up until the heap
                       property is restored.
                       Time: O(log N)

    delete(i)        — Delete the element at index i.
                       Strategy: decrease_key(i, -inf), then extract_min().
                       Time: O(log N)

Array index relationships (0-indexed):
    parent(i)      = (i - 1) // 2
    left_child(i)  = 2 * i + 1
    right_child(i) = 2 * i + 2

Example usage / expected output:

    h = BinaryHeap(20)
    h.insert(4); h.insert(1); h.insert(2); h.insert(6)
    h.insert(7); h.insert(3); h.insert(8); h.insert(5)

    h.get_min()          → 1
    h.insert(-1)
    h.get_min()          → -1
    h.decrease_key(3, -2)
    h.get_min()          → -2
    h.extract_min()
    h.get_min()          → -1
    h.delete(0)
    h.get_min()          → 1
============================================================
"""


class BinaryHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    # ── index helpers ──────────────────────────────────────
    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    # ── operations ─────────────────────────────────────────
    def insert(self, x):
        if self.size == self.capacity:
            print("Binary Heap Overflow")
            return

        self.arr[self.size] = x
        k = self.size
        self.size += 1

        # Bubble up — swap with parent while min-heap property violated
        while k != 0 and self.arr[self.parent(k)] > self.arr[k]:
            self.arr[self.parent(k)], self.arr[k] = self.arr[k], self.arr[self.parent(k)]
            k = self.parent(k)

    def heapify(self, ind):
        li = self.left(ind)
        ri = self.right(ind)
        smallest = ind

        if li < self.size and self.arr[li] < self.arr[smallest]:
            smallest = li
        if ri < self.size and self.arr[ri] < self.arr[smallest]:
            smallest = ri

        if smallest != ind:
            self.arr[ind], self.arr[smallest] = self.arr[smallest], self.arr[ind]
            self.heapify(smallest)

    def get_min(self):
        if self.size == 0:
            return float("inf")
        return self.arr[0]

    def extract_min(self):
        if self.size <= 0:
            return float("inf")
        if self.size == 1:
            self.size -= 1
            return self.arr[0]

        mini = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.size -= 1
        self.heapify(0)
        return mini

    def decrease_key(self, i, val):
        self.arr[i] = val
        while i != 0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[self.parent(i)], self.arr[i] = self.arr[i], self.arr[self.parent(i)]
            i = self.parent(i)

    def delete(self, i):
        self.decrease_key(i, float("-inf"))
        self.extract_min()

    def print_heap(self):
        print(self.arr[:self.size])


# ── driver ──────────────────────────────────────────────────
if __name__ == "__main__":
    h = BinaryHeap(20)
    for v in [4, 1, 2, 6, 7, 3, 8, 5]:
        h.insert(v)

    print("Min value is", h.get_min())   # expected: 1
    h.insert(-1)
    print("Min value is", h.get_min())   # expected: -1
    h.decrease_key(3, -2)
    print("Min value is", h.get_min())   # expected: -2
    h.extract_min()
    print("Min value is", h.get_min())   # expected: -1
    h.delete(0)
    print("Min value is", h.get_min())   # expected: 1
