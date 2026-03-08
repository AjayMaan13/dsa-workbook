"""
PROBLEM: Count the Number of Set Bits
=======================================
Given an integer n, return the number of 1-bits in its binary representation.
Also known as the Hamming weight or popcount.

    n=5  (101)  → 2
    n=15 (1111) → 4
    n=29 (11101) → 4
"""


# ── Brute Force: check each bit via right-shift ──────────────────────────────
# Isolate the LSB with (n & 1), shift right, repeat until n is 0.
# Time: O(log n)  Space: O(1)
def countSetBits_v1(n):
    count = 0
    while n > 0:
        count += (n & 1)  # add 1 if LSB is set
        n >>= 1           # drop the LSB, examine next bit
    return count


# ── Optimal: Brian Kernighan's algorithm  ← use this ────────────────────────
# Key insight: n & (n - 1) clears the lowest set bit of n in one step.
#
#   n = 12  (1100)
#   n-1= 11  (1011)
#   n & (n-1) = 1000   → one set bit removed, count=1
#
#   n = 8   (1000)
#   n-1= 7   (0111)
#   n & (n-1) = 0000   → one set bit removed, count=2  → done
#
# Each iteration eliminates exactly one set bit, so the loop runs only as many
# times as there are set bits — O(number of set bits), which beats O(log n)
# for sparse numbers (few 1s in a large n).
#
# Time: O(number of set bits)  Space: O(1)
def countSetBits(n):
    count = 0
    while n:
        n &= (n - 1)  # clear the lowest set bit
        count += 1
    return count


# ── Tests ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    cases = [
        (5,  2),   # 101
        (15, 4),   # 1111
        (29, 4),   # 11101
        (0,  0),
        (1,  1),
        (8,  1),   # 1000
        (7,  3),   # 111
    ]
    for n, expected in cases:
        assert countSetBits_v1(n) == expected, f"v1 failed for n={n}"
        assert countSetBits(n)    == expected, f"optimal failed for n={n}"
    print("All tests passed ✓")
