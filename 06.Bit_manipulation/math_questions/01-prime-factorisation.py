"""
PROBLEM: Prime Factorisation of a Number
==========================================
Given an integer array queries, return the prime factorisation of each number
in sorted order.

    queries=[2, 3, 4, 5, 6]   → [[2], [3], [2,2], [5], [2,3]]
    queries=[7, 12, 18]        → [[7], [2,2,3], [2,3,3]]
    queries=[15, 20]           → [[3,5], [2,2,5]]
"""


# ── Brute Force: trial division up to n ─────────────────────────────────────
# For each query, check every number from 2 to n as a potential factor.
# Time: O(n) per query  Space: O(log n) for the result
def primeFactors_v1(n):
    factors = []
    for d in range(2, n + 1):      # try every divisor from 2 to n
        while n % d == 0:          # divide out all copies of d
            factors.append(d)
            n //= d
        if n == 1:
            break
    return factors

def solve_v1(queries):
    return [primeFactors_v1(q) for q in queries]


# ── Better: trial division up to sqrt(n) ─────────────────────────────────────
# Any composite n must have a factor ≤ sqrt(n).
# So we only trial-divide up to sqrt(n); if n > 1 remains, it is prime itself.
#
#   n=12: try d=2 → 12/2=6, 6/2=3  → d=3 → 3/3=1  → factors=[2,2,3]
#   n=18: try d=2 → 18/2=9          → d=3 → 9/3=3, 3/3=1 → factors=[2,3,3]
#
# Time: O(sqrt(n)) per query  Space: O(log n)
def primeFactors_v2(n):
    factors = []
    d = 2
    while d * d <= n:              # only go up to sqrt(n)
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:                      # remaining n is a prime factor
        factors.append(n)
    return factors

def solve_v2(queries):
    return [primeFactors_v2(q) for q in queries]


# ── Optimal: Smallest Prime Factor (SPF) Sieve  ← use this ──────────────────
# Best when there are many queries over the same range.
# Precompute the smallest prime factor for every number up to max(queries)
# using a sieve. Then factorise each query in O(log n) by repeatedly dividing
# by its SPF.
#
# SPF sieve (similar to Sieve of Eratosthenes):
#   spf[i] = i initially (each number is its own smallest prime factor)
#   For every prime p found, mark multiples of p that haven't been marked yet.
#
#   i=2: spf[4]=2, spf[6]=2, spf[8]=2, spf[10]=2, spf[12]=2 ...
#   i=3: spf[9]=3, spf[15]=3 (spf[6] already set to 2, skip) ...
#
# Factorisation of n using SPF:
#   n=12 → spf[12]=2 → 12/2=6 → spf[6]=2 → 6/2=3 → spf[3]=3 → done → [2,2,3]
#
# Time: O(N log log N) to build sieve, O(log n) per query  Space: O(N)
def buildSPF(limit):
    spf = list(range(limit + 1))     # spf[i] = i initially
    for i in range(2, int(limit**0.5) + 1):
        if spf[i] == i:              # i is prime (not yet marked)
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:     # only update if not already set
                    spf[j] = i
    return spf

def primeFactors_optimal(n, spf):
    factors = []
    while n > 1:
        factors.append(spf[n])      # smallest prime factor of n
        n //= spf[n]                # divide it out and repeat
    return factors

def solve_optimal(queries):
    if not queries:
        return []
    limit = max(queries)
    spf = buildSPF(limit)
    return [primeFactors_optimal(q, spf) for q in queries]


# ── Tests ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    cases = [
        ([2, 3, 4, 5, 6],  [[2], [3], [2,2], [5], [2,3]]),
        ([7, 12, 18],       [[7], [2,2,3], [2,3,3]]),
        ([15, 20],          [[3,5], [2,2,5]]),
    ]
    for queries, expected in cases:
        assert solve_v1(queries)      == expected, f"v1 failed for {queries}"
        assert solve_v2(queries)      == expected, f"v2 failed for {queries}"
        assert solve_optimal(queries) == expected, f"optimal failed for {queries}"
    print("All tests passed ✓")
