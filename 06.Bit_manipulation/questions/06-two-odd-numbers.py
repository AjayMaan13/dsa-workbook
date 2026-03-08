"""
PROBLEM: Find the Two Numbers Appearing an Odd Number of Times
===============================================================
Given an array where every integer appears twice except for exactly two integers,
find and return those two integers in ascending order.

    nums=[1, 2, 1, 3, 5, 2] → [3, 5]
    nums=[-1, 0]             → [-1, 0]
"""


# ── Brute Force: frequency map ───────────────────────────────────────────────
# Count occurrences of every element; collect those with count == 1.
# Time: O(n)  Space: O(n)
def findTwoOdd_v1(nums):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    result = [n for n, count in freq.items() if count == 1]
    return sorted(result)


# ── Optimal: XOR partitioning  ← use this ────────────────────────────────────
#
# Key XOR properties:
#   x ^ x = 0   (duplicates cancel out)
#   x ^ 0 = x   (identity)
#
# STEP 1 — XOR the entire array
#   All pairs cancel, leaving xor_all = a ^ b
#   where a and b are the two unique numbers.
#
#   nums = [1, 2, 1, 3, 5, 2]
#   xor_all = 1^2^1^3^5^2 = 3^5 = 011^101 = 110
#
# STEP 2 — Find the rightmost set bit of xor_all
#   Since xor_all = a ^ b, any set bit means a and b DIFFER at that position.
#   The rightmost set bit is isolated with: rightmost_bit = xor_all & (-xor_all)
#
#   xor_all = 110  →  rightmost_bit = 010  (bit 1)
#
#   Why (-xor_all) works: negation in two's complement flips all bits then adds 1,
#   which zeros out all bits below the lowest set bit and flips the lowest set bit.
#   AND-ing with the original isolates only that one bit.
#
# STEP 3 — Partition the array using the rightmost set bit
#   Every number either HAS this bit set or DOESN'T.
#   a and b fall into DIFFERENT groups (because they differ at this bit).
#   Within each group, all duplicates still cancel via XOR → two unique numbers.
#
#   bit = 010
#   Has bit:  [2(010), 2(010), 3(011)]  XOR → 3
#   No bit:   [1(001), 1(001), 5(101)]  XOR → 5
#
# Time: O(n)  Space: O(1)
def findTwoOdd(nums):
    # Step 1: XOR all elements → xor_all = a ^ b
    xor_all = 0
    for n in nums:
        xor_all ^= n

    # Step 2: isolate the rightmost set bit (a and b differ here)
    rightmost_bit = xor_all & (-xor_all)

    # Step 3: partition into two groups and XOR each
    a, b = 0, 0
    for n in nums:
        if n & rightmost_bit:   # has the differing bit → group 1
            a ^= n
        else:                   # does not have the bit  → group 2
            b ^= n

    return sorted([a, b])


# ── Tests ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    cases = [
        ([1, 2, 1, 3, 5, 2],       [3, 5]),
        ([-1, 0],                   [-1, 0]),
        ([4, 1, 2, 1, 2, 3, 3, 4, 5, 6], [5, 6]),
        ([10, 10, 7, 3],            [3, 7]),
    ]
    for nums, expected in cases:
        assert findTwoOdd_v1(nums) == expected, f"v1 failed for {nums}"
        assert findTwoOdd(nums)    == expected, f"optimal failed for {nums}"
    print("All tests passed ✓")
