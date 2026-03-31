"""
============================================================
PROBLEM: Convert Min-Heap to Max-Heap
Source  : TakeUForward
============================================================

Given a min-heap represented as an array `nums`, convert it
into a max-heap in-place and return the resulting array.

You do NOT need to sort — just ensure the max-heap property
holds for every node.

Definitions:
  Min-heap: parent ≤ both children  (root = minimum)
  Max-heap: parent ≥ both children  (root = maximum)

Key insight — Heapify approach:
  Treat the array as an unordered complete binary tree.
  Apply build-max-heap using the standard heapify trick:
    - Start from the last non-leaf node: index = (n - 2) // 2
    - Call max_heapify() at each index from there down to 0
    - max_heapify() pushes a node DOWN, swapping with the
      larger child until the max-heap property is restored

  This runs in O(n) — better than inserting one by one.

max_heapify(arr, n, i):
  largest = i
  left  = 2 * i + 1
  right = 2 * i + 2
  if left  < n and arr[left]  > arr[largest]: largest = left
  if right < n and arr[right] > arr[largest]: largest = right
  if largest != i:
      swap arr[i] and arr[largest]
      max_heapify(arr, n, largest)   # recurse down

build_max_heap(arr):
  n = len(arr)
  for i in range((n - 2) // 2, -1, -1):
      max_heapify(arr, n, i)

Time Complexity  : O(n)
Space Complexity : O(log n)  — recursion stack

------------------------------------------------------------
Examples:

  Input : nums = [10, 20, 30, 21, 23]

  As a min-heap tree:         After conversion (one valid max-heap):
        10                              30
       /  \\                           /  \\
      20   30          →             21   23
     /  \\                          /  \\
    21   23                        10   20

  Output: [30, 21, 23, 10, 20]

  ─────────────────────────────────────────────────────────
  Input : nums = [-5, -4, -3, -2, -1]
  Output: [-1, -2, -3, -4, -5]
  (the most negative values sink to the leaves)

  ─────────────────────────────────────────────────────────
  Input : nums = [2, 6, 3, 100, 120, 4, 5]

  🤔 Quiz — pick the correct output:
    (A) [120, 100, 5, 3, 4, 2, 6]
    (B) [100, 120, 6, 3, 4, 2, 5]
    (C) [120, 100, 6, 3, 2, 2, 5]

  Hint: verify your answer by checking the max-heap
  property at every non-leaf node in the output array.
  Answer: (A) [120, 100, 5, 3, 4, 2, 6]

  Note: there can be multiple valid max-heaps for the same
  input. The checker verifies heap property, not exact match.
============================================================
"""


def max_heapify(arr, n, i):
    """Push arr[i] down to its correct position in a max-heap of size n."""
    # YOUR CODE HERE
    pass


def convert_min_to_max_heap(nums):
    """
    Convert the given min-heap array into a max-heap in-place.
    Returns the modified array.
    """
    # YOUR CODE HERE
    pass


# ── helpers ──────────────────────────────────────────────────
def is_max_heap(arr):
    """Verify the array satisfies the max-heap property."""
    n = len(arr)
    for i in range(n // 2):
        left  = 2 * i + 1
        right = 2 * i + 2
        if left  < n and arr[i] < arr[left]:  return False
        if right < n and arr[i] < arr[right]: return False
    return True


# ── tests ────────────────────────────────────────────────────
if __name__ == "__main__":
    tests = [
        [10, 20, 30, 21, 23],
        [-5, -4, -3, -2, -1],
        [2, 6, 3, 100, 120, 4, 5],
        [1],
        [1, 2, 3, 4, 5, 6, 7],
    ]

    all_passed = True
    for nums in tests:
        original = nums[:]
        result = convert_min_to_max_heap(nums[:])  # pass a copy so original is preserved

        if result is None:
            print(f"❌  Input={original}  — returned None (did you forget to return?)")
            all_passed = False
            continue

        valid = is_max_heap(result)
        status = "✅" if valid else "❌"
        if not valid:
            all_passed = False
        print(f"{status}  Input={original}  Output={result}  valid_max_heap={valid}")

    print()
    print("All tests passed!" if all_passed else "Some tests failed — check your heapify logic.")
