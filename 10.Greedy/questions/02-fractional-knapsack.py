# Fractional Knapsack Problem
# (Classic Greedy)
#
# Problem Statement:
# Given N items with weights and values, and a knapsack of capacity W,
# maximize the total value placed in the knapsack. Unlike 0/1 knapsack,
# you can take fractions of an item.
#
# Example 1:
#   Input: val = [60, 100, 120], wt = [10, 20, 30], capacity = 50
#   Output: 240.0
#   Explanation:
#     - Take item 0 fully  (w=10, v=60)
#     - Take item 1 fully  (w=20, v=100)
#     - Take 2/3 of item 2 (w=20, v=80)
#     Total = 240
#
# Example 2:
#   Input: val = [60, 100], wt = [10, 20], capacity = 50
#   Output: 160.0
#   Explanation: Both items fit entirely (10 + 20 = 30 <= 50). Total = 160.


# Greedy - O(n log n) time, O(n) space
# Key insight: always pick the item with the highest value-to-weight ratio first.
# Greedily take as much of it as possible before moving to the next best item.
def fractionalKnapsack(val, wt, capacity):
    # build (ratio, value, weight) tuples for each item
    items = [(val[i] / wt[i], val[i], wt[i]) for i in range(len(val))]

    # sort by value-per-unit-weight descending — best bang-for-buck first
    items.sort(reverse=True)

    total_value = 0.0

    for ratio, value, weight in items:
        if capacity >= weight:
            # take the whole item
            total_value += value
            capacity -= weight
        else:
            # take only the fraction that fits, then stop
            total_value += value * (capacity / weight)
            break

    return total_value


print(fractionalKnapsack([60, 100, 120], [10, 20, 30], 50))  # 240.0
print(fractionalKnapsack([60, 100], [10, 20], 50))            # 160.0
