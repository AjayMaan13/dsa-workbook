"""
============================================================
PROBLEM: Sort a K-Sorted (Nearly Sorted) Array
Source  : TakeUForward
============================================================

Given an array where every element is at most k positions
away from its correct sorted position, sort it efficiently.

Examples:
  arr = [6, 5, 3, 2, 8, 10, 9], k = 3  →  [2, 3, 5, 6, 8, 9, 10]
  arr = [1, 4, 5, 2, 3, 6, 7, 8, 9, 10], k = 2  →  [1,2,3,4,5,6,7,8,9,10]

============================================================
WHY THIS WORKS — THE CORE INSIGHT
============================================================

If every element is at most k positions from its sorted spot,
then the GLOBALLY SMALLEST element must live somewhere in the
first k+1 positions. It cannot be further right.

  arr = [6, 5, 3, 2, 8, 10, 9],  k = 3

  Sorted : [2, 3, 5, 6, 8, 9, 10]
  Element 2 belongs at index 0.
  In original array, it is at index 3.
  Distance = 3 = k  ✅  (within first k+1 = 4 positions)

So at any point, if we maintain a min-heap of the next k+1
elements, the ROOT is guaranteed to be the next sorted value.

============================================================
SLIDING WINDOW + MIN-HEAP VISUAL
============================================================

arr = [6, 5, 3, 2, 8, 10, 9],  k = 3
Window size = k + 1 = 4

── Seed: push first k+1 = 4 elements ──────────────────────

  push 6 → heap: [6]
  push 5 → heap: [5, 6]
  push 3 → heap: [3, 6, 5]
  push 2 → heap: [2, 6, 5, 3]   ← root = 2 (the min)

  Window on array:
  [6, 5, 3, 2] | 8, 10, 9
   ^^^^^^^^^^^
     in heap

── Process remaining elements one by one ───────────────────

  i=4, element=8:
    pop  root(2)  → result: [2]
    push 8        → heap: [3, 6, 5, 8]

    Window: 6, [5, 3, 2, 8] | 10, 9
                 ^^^^^^^^^^^
                   in heap

  i=5, element=10:
    pop  root(3)  → result: [2, 3]
    push 10       → heap: [5, 6, 8, 10]  (min-heap re-ordered)

    Window: 6, 5, [3, 2, 8, 10] | 9

  i=6, element=9:
    pop  root(5)  → result: [2, 3, 5]
    push 9        → heap: [6, 9, 8, 10]

    Window: 6, 5, 3, [2, 8, 10, 9]

── Drain remaining heap ────────────────────────────────────

  pop 6  → result: [2, 3, 5, 6]
  pop 8  → result: [2, 3, 5, 6, 8]
  pop 9  → result: [2, 3, 5, 6, 8, 9]
  pop 10 → result: [2, 3, 5, 6, 8, 9, 10]  ✅

============================================================
WHY WINDOW SIZE IS k+1 AND NOT k
============================================================

  Element can be at most k positions to the LEFT of its target.
  So in the worst case the minimum is at index k (0-based).
  That means we need indices 0..k  →  k+1 elements in the heap.

  Example: k=3, minimum at index 3 → need indices 0,1,2,3 = 4 = k+1

============================================================
COMPLEXITY
============================================================

  Brute Force  : sort() → O(n log n) time, O(1) space (ignores k)
  Optimal      : heap   → O(n log k) time, O(k) space

  The heap never holds more than k+1 elements.
  Every push/pop on a heap of size k+1 costs O(log(k+1)) = O(log k).
  We do this n times → O(n log k).

  When k << n this is much better than O(n log n).
  E.g. k=10, n=1,000,000 → log k ≈ 3 vs log n ≈ 20.

============================================================
"""

import heapq


# ── Brute Force ──────────────────────────────────────────────
def sort_k_sorted_brute(arr, k):
    """
    Ignores the k constraint entirely.
    Just sorts the full array — O(n log n).
    """
    return sorted(arr)


# ── Optimal: Min-Heap Sliding Window ─────────────────────────
def sort_k_sorted_optimal(arr, k):
    """
    Uses a min-heap of size k+1.
    At every step the root is the next element for the result.

    Steps:
      1. Push first k+1 elements into the heap.
      2. For each remaining element:
           - Pop root → append to result
           - Push current element into heap
      3. Drain remaining heap into result.
    """
    heap  = []
    result = []

    # Step 1: seed the heap with the first window
    for i in range(min(k + 1, len(arr))):
        heapq.heappush(heap, arr[i])

    # Step 2: slide the window across the rest of the array
    for i in range(k + 1, len(arr)):
        result.append(heapq.heappop(heap))   # smallest in window → result
        heapq.heappush(heap, arr[i])         # bring next element into window

    # Step 3: drain whatever's left in the heap
    while heap:
        result.append(heapq.heappop(heap))

    return result


# ── tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    tests = [
        ([6, 5, 3, 2, 8, 10, 9],          3, [2, 3, 5, 6, 8, 9, 10]),
        ([1, 4, 5, 2, 3, 6, 7, 8, 9, 10], 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([10, 9, 8, 7, 4, 70, 60, 50],    4, [4, 7, 8, 9, 10, 50, 60, 70]),
        ([1],                              0, [1]),
        ([2, 1],                           1, [1, 2]),
    ]

    print("=" * 65)
    print(f"{'Result':<6} {'Input':<35} {'k':<4} {'Expected'}")
    print("=" * 65)

    all_ok = True
    for arr, k, expected in tests:
        brute   = sort_k_sorted_brute(arr[:], k)
        optimal = sort_k_sorted_optimal(arr[:], k)
        ok = optimal == expected and brute == expected
        status = "✅" if ok else "❌"
        if not ok:
            all_ok = False
        print(f"{status}     arr={arr}")
        print(f"       k={k}  →  got={optimal}  expected={expected}")
        print()

    print("=" * 65)
    print("All tests passed! ✅" if all_ok else "Some tests failed ❌")