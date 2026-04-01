"""
Problem: Replace elements by their rank in the array

Given an array of integers, replace each element with its rank when the array
is sorted in ascending order.

Rules:
- Rank starts from 1
- Smaller number → smaller rank
- Duplicate elements share the same rank

Examples:
Input:  [20, 15, 26, 2, 98, 6]
Output: [4, 3, 5, 1, 6, 2]

Input:  [1, 5, 8, 15, 8, 25, 9]
Output: [1, 2, 3, 5, 3, 6, 4]
"""


# -------------------------------
# 🔴 Brute Force Approach
# -------------------------------
# Idea:
# For each element, count how many UNIQUE elements are smaller than it.
# Rank = count of unique smaller elements + 1
#
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class BruteForceSolution:
    def replaceWithRank(self, arr):
        result = []

        for i in range(len(arr)):
            smaller = set()

            for j in range(len(arr)):
                if arr[j] < arr[i]:
                    smaller.add(arr[j])  # keep only unique values

            rank = len(smaller) + 1
            result.append(rank)

        return result


# -------------------------------
# 🟢 Optimal Approach (Sorting + Map)
# -------------------------------
# Idea:
# 1. Sort the array
# 2. Assign ranks to unique elements
# 3. Use a dictionary to map value → rank
# 4. Build result using that map
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class OptimalSolution:
    def replaceWithRank(self, arr):
        sorted_arr = sorted(arr)

        rank_map = {}
        rank = 1

        for num in sorted_arr:
            if num not in rank_map:   # avoid duplicates
                rank_map[num] = rank
                rank += 1

        return [rank_map[num] for num in arr]


# -------------------------------
# 🔵 (Optional) Heap-Based Approach
# -------------------------------
# Idea:
# Use a min-heap to process elements in sorted order
# Similar to sorting, but explicitly uses heap
#
# Time Complexity: O(n log n)

import heapq

class HeapSolution:
    def replaceWithRank(self, arr):
        heap = []

        # push all elements into heap
        for num in arr:
            heapq.heappush(heap, num)

        rank_map = {}
        rank = 1

        # assign ranks in sorted order
        while heap:
            num = heapq.heappop(heap)
            if num not in rank_map:
                rank_map[num] = rank
                rank += 1

        return [rank_map[num] for num in arr]


# -------------------------------
# ✅ Test Runner
# -------------------------------
if __name__ == "__main__":
    arr1 = [20, 15, 26, 2, 98, 6]
    arr2 = [1, 5, 8, 15, 8, 25, 9]

    print("Brute Force:")
    print(BruteForceSolution().replaceWithRank(arr1))
    print(BruteForceSolution().replaceWithRank(arr2))

    print("\nOptimal:")
    print(OptimalSolution().replaceWithRank(arr1))
    print(OptimalSolution().replaceWithRank(arr2))

    print("\nHeap:")
    print(HeapSolution().replaceWithRank(arr1))
    print(HeapSolution().replaceWithRank(arr2))