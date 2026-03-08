"""
PROBLEM: Check if the i-th Bit is Set
=======================================
Given n and i, return True if the i-th bit (0-indexed from LSB) of n is 1.

    n=5  (101),  i=0 → True   (LSB is 1)
    n=10 (1010), i=1 → True
    n=5  (101),  i=1 → False
"""


# ── Brute Force: convert to binary string ──────────────────────────────────
# Time: O(log n)  Space: O(log n)
def checkIthBit_v1(n, i):
    binary = bin(n)[2:]             # e.g. 5 → "101"
    if i >= len(binary):
        return False
    return binary[-(i + 1)] == '1' # index from right


# ── Optimal: bit masking  ← use this ───────────────────────────────────────
# Shift 1 left by i to create a mask with only the i-th bit set,
# then AND with n. Non-zero result means the bit is set.
#
#   n=5 (101), i=2:  1 << 2 = 100  →  101 & 100 = 100 ≠ 0  → True
#   n=5 (101), i=1:  1 << 1 = 010  →  101 & 010 = 000 = 0  → False
#
# Time: O(1)  Space: O(1)
def checkIthBit(n, i):
    return (n & (1 << i)) != 0


# ── Tests ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    cases = [(5,0,True),(10,1,True),(5,1,False),(5,2,True),(8,3,True),(7,3,False)]
    for n, i, expected in cases:
        assert checkIthBit_v1(n, i) == expected
        assert checkIthBit(n, i)    == expected
    print("All tests passed ✓")