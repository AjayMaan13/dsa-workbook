"""
PROBLEM: Set the Rightmost Unset Bit
======================================
Given a positive integer n, set the rightmost 0-bit to 1 and return the result.
If all bits in n's representation are already 1, return n unchanged.

    n=10 (1010) → 11 (1011)   rightmost 0 is bit 0, set it
    n=12 (1100) → 13 (1101)   rightmost 0 is bit 1, set it
    n=7  (0111) →  7 (0111)   all bits set, return as-is
"""


# ── Brute Force: scan bits from LSB ─────────────────────────────────────────
# Iterate through each bit position; as soon as a 0-bit is found, set it.
# Time: O(log n)  Space: O(1)
def setRightmostUnsetBit_v1(n):
    i = 0
    while n >> i:          # stop when no more bits remain
        if not (n >> i & 1):   # bit i is 0 → set it
            return n | (1 << i)
        i += 1
    return n               # all bits were 1


# ── Optimal: n | (n + 1)  ← use this ────────────────────────────────────────
# Key insight: adding 1 to n flips the rightmost 0-bit to 1 and zeros all
# trailing 1-bits to the right of it. OR-ing restores the original bits while
# keeping that newly flipped bit set.
#
#   n = 10  (1010)
#   n+1= 11  (1011)   rightmost 0 (bit 0) flipped → 1
#   n | (n+1)= 1011  = 11  ✓
#
#   n = 12  (1100)
#   n+1= 13  (1101)   rightmost 0 (bit 1) flipped → 1, trailing 1s zeroed
#   n | (n+1)= 1101  = 13  ✓
#
# Edge case: if n is all 1s (e.g. 0111), n+1 carries into a new bit position
# (1000), and OR would incorrectly grow the number. Detect this with
# (n & (n+1)) == 0, which is true only when n = 2^k - 1 (all 1s pattern).
#
# Time: O(1)  Space: O(1)
def setRightmostUnsetBit(n):
    if (n & (n + 1)) == 0:  # all bits already set (n is of form 2^k - 1)
        return n
    return n | (n + 1)


# ── Tests ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    cases = [
        (10, 11),   # 1010 → 1011
        (12, 13),   # 1100 → 1101
        (7,   7),   # 0111 → all set, unchanged
        (1,   3),   # 01   → 11
        (6,   7),   # 110  → 111
        (15, 15),   # 1111 → all set, unchanged
    ]
    for n, expected in cases:
        assert setRightmostUnsetBit_v1(n) == expected, f"v1 failed for n={n}"
        assert setRightmostUnsetBit(n)    == expected, f"optimal failed for n={n}"
    print("All tests passed ✓")
