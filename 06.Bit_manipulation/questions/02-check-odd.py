"""
PROBLEM: Check if a Number is Odd
===================================
Given an integer n, return True if n is odd, False if even.
Use bit manipulation — do NOT use the modulo operator.

    n=5  (101) → True   (LSB is 1 → odd)
    n=4  (100) → False  (LSB is 0 → even)
    n=7  (111) → True
    n=0  (000) → False
"""


# ── Brute Force: modulo operator ────────────────────────────────────────────
# Time: O(1)  Space: O(1)
def isOdd_v1(n):
    return n % 2 != 0


# ── Optimal: bit masking  ← use this ────────────────────────────────────────
# The least-significant bit (bit 0) of any integer is 1 for odd, 0 for even.
# AND-ing with 1 isolates that bit.
#
#   n=5 (101):  101 & 001 = 001 = 1  → odd  → True
#   n=4 (100):  100 & 001 = 000 = 0  → even → False
#
# Works correctly for negative numbers too because their LSB still encodes parity.
#
# Time: O(1)  Space: O(1)
def isOdd(n):
    return (n & 1) == 1


# ── Tests ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    cases = [
        (5,  True),
        (4,  False),
        (7,  True),
        (0,  False),
        (1,  True),
        (-3, True),
        (-4, False),
    ]
    for n, expected in cases:
        assert isOdd_v1(n) == expected
        assert isOdd(n)    == expected
    print("All tests passed ✓")
