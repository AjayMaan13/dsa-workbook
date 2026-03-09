"""
PROBLEM: Sieve of Eratosthenes — Count Primes in Range
========================================================
Given a 2D array queries where each query is [L, R], return the count of
prime numbers in the inclusive range [L, R] for each query.

    queries=[[2,5],[4,7]]  → [3, 2]   (primes: {2,3,5}, {5,7})
    queries=[[1,7],[3,7]]  → [4, 3]   (primes: {2,3,5,7}, {3,5,7})
"""


# ── Brute Force: check each number per query ─────────────────────────────────
# For every query [L, R], test each number in the range for primality.
# Primality check: trial division up to sqrt(n).
# Time: O(q * R * sqrt(R))  Space: O(1)
def isPrime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def primesInRange_v1(queries):
    result = []
    for L, R in queries:
        count = sum(1 for n in range(L, R + 1) if isPrime(n))
        result.append(count)
    return result


# ── Optimal: Sieve of Eratosthenes + Prefix Sum  ← use this ─────────────────
# Build a sieve ONCE, then answer every query in O(1) using a prefix sum.
#
# STEP 1 — Sieve of Eratosthenes up to max(queries)
#   Start with all numbers marked as prime.
#   For each prime p (starting at 2), mark all its multiples as NOT prime.
#   Only iterate up to sqrt(max_val) — any composite must have a factor ≤ sqrt.
#   Start marking from p*p (all smaller multiples already marked by earlier primes).
#
#   max_val=10:
#   Initial:   [F, F, T, T, T, T, T, T, T, T, T]  (0,1 → not prime)
#   p=2:       mark 4,6,8,10 → [F,F,T,T,F,T,F,T,F,T,F]
#   p=3:       mark 9        → [F,F,T,T,F,T,F,T,F,F,F]
#   (p=4: not prime, skip)
#   Primes: 2,3,5,7
#
# STEP 2 — Build prefix sum
#   prime_count[i] = number of primes in [0..i]
#   Allows any range [L, R] to be answered in O(1):
#       count = prime_count[R] - prime_count[L-1]
#
#   i:           0  1  2  3  4  5  6  7
#   is_prime:    F  F  T  T  F  T  F  T
#   prime_count: 0  0  1  2  2  3  3  4
#
#   query [2,5]: prime_count[5] - prime_count[1] = 3 - 0 = 3  ✓
#   query [4,7]: prime_count[7] - prime_count[3] = 4 - 2 = 2  ✓
#
# Time: O(N log log N) sieve + O(N) prefix sum + O(1) per query
# Space: O(N)
def primesInRange(queries):
    if not queries:
        return []

    max_val = max(R for _, R in queries)

    # Step 1: sieve — mark all primes up to max_val
    is_prime = [True] * (max_val + 1)
    is_prime[0] = is_prime[1] = False      # 0 and 1 are not prime

    p = 2
    while p * p <= max_val:
        if is_prime[p]:                    # p is prime
            for multiple in range(p * p, max_val + 1, p):
                is_prime[multiple] = False # mark composites
        p += 1

    # Step 2: prefix sum — prime_count[i] = # primes in [0..i]
    prime_count = [0] * (max_val + 1)
    for i in range(1, max_val + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    # Step 3: answer each query in O(1)
    result = []
    for L, R in queries:
        if L == 0:
            result.append(prime_count[R])
        else:
            result.append(prime_count[R] - prime_count[L - 1])

    return result


# ── Tests ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    cases = [
        ([[2, 5], [4, 7]],  [3, 2]),
        ([[1, 7], [3, 7]],  [4, 3]),
        ([[0, 10]],         [4]),    # primes: 2,3,5,7
        ([[1, 1]],          [0]),
        ([[2, 2]],          [1]),
    ]
    for queries, expected in cases:
        assert primesInRange_v1(queries) == expected, f"v1 failed for {queries}"
        assert primesInRange(queries)    == expected, f"optimal failed for {queries}"
    print("All tests passed ✓")
