"""
============================================================
PROBLEM: Check if an Array Represents a Min-Heap
Source  : TakeUForward
============================================================

Given an array of integers `nums`, return True if the array
is a valid binary min-heap, otherwise return False.

A binary min-heap is a complete binary tree where:
  - The key at the root is the minimum among all keys.
  - This property holds recursively for every node.

In array form (0-indexed), for a node at index i:
  - Left child  → 2 * i + 1
  - Right child → 2 * i + 2
  - Parent      → (i - 1) // 2

Key insight:
  Leaf nodes (index >= n // 2) have no children, so they
  can never violate the heap property. You only need to
  check non-leaf nodes: indices 0 to (n // 2 - 1).

For each non-leaf node at index i:
  - If its left child exists  AND nums[left]  < nums[i] → not a min-heap
  - If its right child exists AND nums[right] < nums[i] → not a min-heap

Algorithm:
  1. Iterate i from 0 to n // 2 - 1  (non-leaf nodes only)
  2. Compute left  = 2 * i + 1
  3. Compute right = 2 * i + 2
  4. If left  < n  and nums[i] > nums[left]:  return False
  5. If right < n  and nums[i] > nums[right]: return False
  6. Return True

Time Complexity  : O(n)
Space Complexity : O(1)

------------------------------------------------------------
Examples:

  Input : nums = [10, 20, 30, 21, 23]
  Output: True
  Reason: Every parent ≤ both children.

        10
       /  \\
      20   30
     /  \\
    21   23

  Input : nums = [10, 20, 30, 25, 15]
  Output: False
  Reason: Node 20 (index 1) has right child 15 (index 4),
          but 15 < 20 — violates min-heap property.

        10
       /  \\
      20   30
     /  \\
    25   15   ← 15 < 20, violation!
============================================================
"""


class Solution:
    def isMinHeap(self, nums):
        # YOUR CODE HERE
        pass


# ── tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([10, 20, 30, 21, 23],        True),   # valid min-heap
        ([10, 20, 30, 25, 15],        False),  # violation at node 20 → child 15
        ([1],                         True),   # single element
        ([1, 2, 3, 4, 5, 6, 7],      True),   # perfect min-heap
        ([1, 3, 2, 7, 4, 6, 5],      True),   # valid — not unique ordering
        ([5, 10, 3, 20, 25],          False),  # root 5 > right child 3
        ([2, 6, 3, 100, 120, 4, 5],  False),  # 3 (index 2) has child 4 (index 5), ok
                                               # but 6 (index 1) has child 100,120 ok
                                               # actually: need to check carefully ↑
    ]

    all_passed = True
    for nums, expected in tests:
        result = sol.isMinHeap(nums)
        status = "✅" if result == expected else "❌"
        if result != expected:
            all_passed = False
        print(f"{status}  nums={nums}  expected={expected}  got={result}")

    print()
    print("All tests passed!" if all_passed else "Some tests failed — review your logic.")
