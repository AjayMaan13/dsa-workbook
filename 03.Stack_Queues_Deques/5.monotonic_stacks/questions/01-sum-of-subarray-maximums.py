# Sum of Subarray Maximums
#
# Given an array, return the sum of the maximum value across every
# possible subarray, modulo 10^9 + 7.
#
# Example:
#   arr = [2, 3, 1, 2, 4]
#   Subarrays and their maxes:
#     [2]→2, [3]→3, [1]→1, [2]→2, [4]→4
#     [2,3]→3, [3,1]→3, [1,2]→2, [2,4]→4
#     [2,3,1]→3, [3,1,2]→3, [1,2,4]→4
#     [2,3,1,2]→3, [3,1,2,4]→4
#     [2,3,1,2,4]→4
#   Output: 45
#
# Strategy — Contribution Technique  O(n) time, O(n) space
#
# For each element arr[i], count how many subarrays have it as the maximum,
# then multiply: contribution = arr[i] * left[i] * right[i]
#
#   left[i]  = number of subarrays ending at i   where arr[i] is the max
#            = distance to the previous element >= arr[i]  (or start of array)
#
#   right[i] = number of subarrays starting at i where arr[i] is the max
#            = distance to the next element > arr[i]       (or end of array)
#
# Tie-breaking: attribute equal-element subarrays to the RIGHTMOST occurrence.
#   Left pass  uses strict <  (pops smaller, keeps >=)
#   Right pass uses       <=  (pops smaller-or-equal, keeps strictly greater)


class Solution(object):
    def sumSubarrayMaxs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(arr)
        left  = [0] * n
        right = [0] * n

        # Left pass — find distance to previous element >= arr[i]
        stack = []
        for i in range(n):
            cur = arr[i]
            while stack and arr[stack[-1]] < cur:   # strict <
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        # Right pass — find distance to next element strictly > arr[i]
        # Must iterate RIGHT TO LEFT (the original bug: this was a copy of the left pass)
        stack = []
        for i in range(n - 1, -1, -1):
            cur = arr[i]
            while stack and arr[stack[-1]] <= cur:  # <= to handle ties
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        res = sum(arr[i] * left[i] * right[i] for i in range(n))
        return res % MOD


arr = [2, 3, 1, 2, 4]
sol = Solution()
print(sol.sumSubarrayMaxs(arr))   # 45

# Contribution breakdown:
# arr[0]=2: left=1, right=1  → 2×1×1 =  2
# arr[1]=3: left=2, right=3  → 3×2×3 = 18
# arr[2]=1: left=1, right=1  → 1×1×1 =  1
# arr[3]=2: left=2, right=1  → 2×2×1 =  4
# arr[4]=4: left=5, right=1  → 4×5×1 = 20
# Total = 2+18+1+4+20 = 45 ✓
