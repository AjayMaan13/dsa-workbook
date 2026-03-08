"""
PROBLEM: Swap Two Numbers Without a Temporary Variable
=======================================================
Given two integers a and b, swap them in-place using only XOR bit manipulation.

    a=5,    b=10   → a=10,   b=5
    a=-100, b=-200 → a=-200, b=-100
"""


# ── Brute Force: temporary variable ─────────────────────────────────────────
# Simple and readable, but uses an extra variable.
# Time: O(1)  Space: O(1)
def swap_v1(a, b):
    temp = a
    a = temp
    b = temp
    return a, b


# ── Optimal: XOR swap  ← use this ───────────────────────────────────────────
# XOR properties that make this work:
#   1. x ^ x = 0       (a number XORed with itself is 0)
#   2. x ^ 0 = x       (a number XORed with 0 is itself)
#   3. XOR is commutative and associative
#
# Walkthrough with a=5 (0101), b=10 (1010):
#
#   Step 1 — a = a ^ b
#            a = 0101 ^ 1010 = 1111  (a now holds XOR of both)
#
#   Step 2 — b = a ^ b
#            b = 1111 ^ 1010 = 0101  (XOR cancels b's bits → original a=5)
#
#   Step 3 — a = a ^ b
#            a = 1111 ^ 0101 = 1010  (XOR cancels a's bits → original b=10)
#
# Why no temp needed: the XOR value in step 1 acts as an encoded combination
# of both numbers. Each subsequent XOR "subtracts" one of them out.
#
# ⚠ Edge case: if a and b point to the same variable (a is b), all three XORs
# produce 0, wiping the value. Always guard against self-swap if needed.
#
# Time: O(1)  Space: O(1)
def swap(a, b):
    a = a ^ b   # a holds XOR of both original values
    b = a ^ b   # b ^ (a^b) = a  → b is now original a
    a = a ^ b   # (a^b) ^ a = b  → a is now original b
    return a, b


# ── Tests ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    cases = [
        (5,    10,   10,   5),
        (-100, -200, -200, -100),
        (0,    7,    7,    0),
        (42,   42,   42,   42),   # same value (not same variable — safe)
        (-1,   1,    1,    -1),
    ]
    for a, b, exp_a, exp_b in cases:
        ra, rb = swap(a, b)
        assert (ra, rb) == (exp_a, exp_b), f"failed for a={a}, b={b}"
    print("All tests passed ✓")
