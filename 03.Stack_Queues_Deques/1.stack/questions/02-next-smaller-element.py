'''
5. Next Smaller Element

Problem Statement: Given an array of integers arr, your task is to find the Next Smaller Element (NSE)
for every element in the array.
The Next Smaller Element for an element x is defined as the first element to the right of x that is
smaller than x.
If there is no smaller element to the right, then the NSE is -1.

Examples:
    Input:  arr = [4, 8, 5, 2, 25]
    Output: [2, 5, 2, -1, -1]

    Input:  arr = [10, 9, 8, 7]
    Output: [9, 8, 7, -1]
'''


# ─── Brute Force ────────────────────────────────────────────────────────────────
# For each element, scan every element to its right and find the first one smaller.
#
# Time Complexity : O(n²)
# Space Complexity: O(1)  (output array not counted)

def next_smaller_brute(arr):
    n = len(arr)
    result = []
    for i in range(n):
        nse = -1
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                nse = arr[j]
                break
        result.append(nse)
    return result


# ─── Optimal (Monotonic Stack) ───────────────────────────────────────────────────
# Traverse right to left, maintaining a stack of candidates in increasing order
# from top to bottom. For each element:
#   1. Pop elements from the stack that are >= current element (they can never be
#      the NSE for current or any future element to the left).
#   2. The stack top (if any) is the NSE for the current element.
#   3. Push the current element onto the stack.
#
# Time Complexity : O(n)  — each element is pushed and popped at most once
# Space Complexity: O(n)  — stack

def next_smaller_optimal(arr):
    n = len(arr)
    result = [-1] * n
    stack = []  # monotonic increasing stack (bottom → top: larger → smaller)

    for i in range(n - 1, -1, -1):
        # remove elements that are >= arr[i]; they're useless for elements to the left
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]  # top is the first smaller element to the right

        stack.append(arr[i])

    return result


# ─── Driver ──────────────────────────────────────────────────────────────────────
arr1 = [4, 8, 5, 2, 25]
arr2 = [10, 9, 8, 7]

print(next_smaller_brute(arr1))    # [2, 5, 2, -1, -1]
print(next_smaller_brute(arr2))    # [9, 8, 7, -1]

print(next_smaller_optimal(arr1))  # [2, 5, 2, -1, -1]
print(next_smaller_optimal(arr2))  # [9, 8, 7, -1]
