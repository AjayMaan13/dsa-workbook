"""
============================================================
PROBLEM: Kth Largest Element in an Array
Source  : TakeUForward / LeetCode 215
============================================================

Given an array nums and an integer k, return the Kth largest
element in the array (not the Kth distinct element).

Examples:
  Input : nums = [1, 2, 3, 4, 5], k = 2  →  Output: 4
  Input : nums = [-5, 4, 1, 2, -3], k = 5 → Output: -5

============================================================
APPROACH 1 — MIN-HEAP OF SIZE K
============================================================

CORE IDEA:
  Keep a min-heap that holds exactly the K largest elements
  seen so far. The ROOT of this heap is always the smallest
  of those K elements — i.e., the Kth largest overall.

WHY A MIN-HEAP?
  We want to quickly find and EVICT the weakest element
  whenever a stronger one comes in. The min-heap gives us
  O(1) access to the minimum (the weakest of the top-K).

VISUAL WALKTHROUGH:
  nums = [3, 1, 5, 2, 4],  k = 2
  Goal : Find the 2nd largest → answer is 4

  ── Phase 1: Fill heap with first k=2 elements ──

    push 3 → heap:
                3          ← only element

    push 1 → heap (min-heap, smaller floats up):
                1
               /
              3

    heap as array: [1, 3]
                    ↑
                  root = current "2nd largest" guess = 1

  ── Phase 2: Process remaining elements ──

    See 5 → Is 5 > root(1)? YES
              pop 1, push 5
              heap:
                3
               /
              5
              re-heapify →
                3
               /
              5     → [3, 5]   root = 3

    See 2 → Is 2 > root(3)? NO → skip

    See 4 → Is 4 > root(3)? YES
              pop 3, push 4
              heap:
                4
               /
              5
              re-heapify →
                4
               /
              5     → [4, 5]   root = 4

  ── Answer: root = pq[0] = 4 ✅ ──

  At every step, the heap holds the 2 largest seen so far.
  The root is always the WEAKEST of those → the Kth largest.

Time : O(n log k)  — n elements, each heap op costs log k
Space: O(k)        — heap never grows beyond size k
"""

import heapq


def kth_largest_heap(nums, k):
    pq = []

    # ── Phase 1: seed the heap with first k elements ──
    for i in range(k):
        heapq.heappush(pq, nums[i])
    # pq is now a min-heap of size k
    # pq[0] = smallest of the k elements seen = current Kth largest guess

    # ── Phase 2: slide through the rest ──
    for i in range(k, len(nums)):
        # pq[0] is the root (minimum of the heap)
        if nums[i] > pq[0]:
            heapq.heappop(pq)           # evict the weakest of top-k
            heapq.heappush(pq, nums[i]) # bring in the new stronger element

    # Root of the heap = Kth largest
    return pq[0]


"""
============================================================
APPROACH 2 — QUICKSELECT  (O(n) average)
============================================================

CORE IDEA:
  Like QuickSort — pick a pivot, partition the array so
  everything GREATER than pivot is on the LEFT, everything
  SMALLER is on the RIGHT. The pivot then sits at its
  correct index in a "descending sorted" array.

  If pivot lands at index k-1 → that's the Kth largest!
  Otherwise recurse on just ONE side (not both like QuickSort).

KEY INSIGHT — why descending?
  We want the Kth LARGEST, so we sort conceptually like:
  index 0 = largest, index 1 = 2nd largest, ..., index k-1 = Kth largest

PARTITION STEP VISUAL:
  nums = [3, 1, 5, 2, 4],  pivot = 3 (index 0),  left=0, right=4

  Step 1: Swap pivot to the left edge (it's already there)
    [3,  1,  5,  2,  4]
     ↑ pivot at left=0

  Step 2: ind = left+1 = 1  (marks where next "greater" goes)
    Scan i from left+1 to right:

    i=1, nums[1]=1 → 1 > pivot(3)? NO  → skip
         [3, 1, 5, 2, 4]   ind=1

    i=2, nums[2]=5 → 5 > pivot(3)? YES → swap nums[ind] ↔ nums[i]
         [3, 5, 1, 2, 4]   ind→2

    i=3, nums[3]=2 → 2 > pivot(3)? NO  → skip
         [3, 5, 1, 2, 4]   ind=2

    i=4, nums[4]=4 → 4 > pivot(3)? YES → swap nums[ind] ↔ nums[i]
         [3, 5, 4, 2, 1]   ind→3

  Step 3: Place pivot at ind-1=2  (swap nums[left] ↔ nums[ind-1])
    swap nums[0] ↔ nums[2]
         [4, 5, 3, 2, 1]
                ↑
           pivot(3) at index 2

  Everything left  of index 2: [4, 5]  all > 3  ✅
  Everything right of index 2: [2, 1]  all < 3  ✅

QUICKSELECT DECISION (k=2, target index = k-1 = 1):
  pivot landed at index 2
  2 > 1  →  answer is in LEFT portion → set right = 2-1 = 1

  Next search on [4, 5] (indices 0..1)
  pivot = 4, lands at index 1 = k-1 = 1  →  return nums[1] = 4  ✅

Time : O(n) average,  O(n²) worst (rare with random pivot)
Space: O(1) — sorts in-place
"""

import random


def kth_largest_quickselect(nums, k):
    nums = nums[:]          # work on a copy so we don't mutate the input
    left, right = 0, len(nums) - 1

    while True:
        # Random pivot avoids O(n²) worst case on already-sorted input
        pivot_index = random.randint(left, right)

        # Partition and find where pivot actually ends up
        pivot_index = _partition(nums, pivot_index, left, right)

        if pivot_index == k - 1:        # pivot is exactly the Kth largest
            return nums[pivot_index]
        elif pivot_index > k - 1:       # answer is to the LEFT
            right = pivot_index - 1
        else:                           # answer is to the RIGHT
            left = pivot_index + 1


def _partition(nums, pivot_index, left, right):
    pivot = nums[pivot_index]

    # Move pivot to the left edge temporarily
    nums[left], nums[pivot_index] = nums[pivot_index], nums[left]

    ind = left + 1  # everything before ind is > pivot

    for i in range(left + 1, right + 1):
        if nums[i] > pivot:             # belongs in the "greater" zone
            nums[ind], nums[i] = nums[i], nums[ind]
            ind += 1

    # Slot pivot into its final correct position
    nums[left], nums[ind - 1] = nums[ind - 1], nums[left]

    return ind - 1  # pivot's final index


"""
============================================================
COMPARISON SUMMARY
============================================================

                  HEAP                    QUICKSELECT
────────────────────────────────────────────────────────────
Idea        Keep top-K in min-heap    Partition like QuickSort,
            root = Kth largest        only go down ONE side

Time        O(n log k) guaranteed     O(n) avg, O(n²) worst

Space       O(k)                      O(1) in-place

Mutates     No                        Yes (we copy here)
input?

Interview   ✅ Lead with this when    ✅ Mention as O(n) follow-up
tip         problem mentions heap     if asked to optimize

============================================================
"""


# ── tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5],   2,  4),
        ([-5, 4, 1, 2, -3], 5, -5),
        ([3, 2, 1, 5, 6, 4], 2,  5),
        ([1],               1,  1),
        ([7, 7, 7, 7],      2,  7),
    ]

    print("=" * 55)
    print(f"{'Test':<30} {'Heap':>8} {'QSelect':>8} {'Expected':>8}")
    print("=" * 55)

    all_ok = True
    for nums, k, expected in tests:
        h = kth_largest_heap(nums[:], k)
        q = kth_largest_quickselect(nums[:], k)
        ok = h == expected and q == expected
        status = "✅" if ok else "❌"
        if not ok:
            all_ok = False
        print(f"{status} nums={nums}, k={k:<5} {h:>8} {q:>8} {expected:>8}")

    print("=" * 55)
    print("All tests passed! ✅" if all_ok else "Some tests failed ❌")