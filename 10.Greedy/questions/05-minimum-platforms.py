# Minimum Number of Platforms Required for a Railway Station
#
# Given arrival and departure times of N trains, find the minimum number
# of platforms needed so no train has to wait.
#
# Examples:
#   arr = [9:00, 9:45, 9:55, 11:00, 15:00, 18:00]
#   dep = [9:20, 12:00, 11:30, 11:50, 19:00, 20:00]
#   Output: 3
#   (trains at 9:45 and 9:55 haven't departed when 11:00 arrives → 3 at once)
#
#   arr = [10:20, 12:00]
#   dep = [10:50, 12:30]
#   Output: 1
#   (first train gone before second arrives)

# ------------------------------------------------------------
# BRUTE FORCE  —  O(n^2) time | O(1) space
# ------------------------------------------------------------
# For each train i, count how many other trains overlap with it
# (arrived but not yet departed). Track the maximum overlap.
#
# A train j overlaps with train i when:
#   arr[j] <= arr[i] <= dep[j]

def min_platforms_brute(arr, dep):
    n = len(arr)
    max_platforms = 1

    for i in range(n):
        platforms = 1   # platform for train i itself
        for j in range(n):
            if i != j:
                # train j is at the station when train i arrives
                if arr[j] <= arr[i] <= dep[j]:
                    platforms += 1
        max_platforms = max(max_platforms, platforms)

    return max_platforms


arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]
print(min_platforms_brute(arr, dep))   # 3

arr2 = [1020, 1200]
dep2 = [1050, 1230]
print(min_platforms_brute(arr2, dep2))  # 1


# ------------------------------------------------------------
# OPTIMAL  —  O(n log n) time | O(1) space
# ------------------------------------------------------------
# Key insight: treat arrivals and departures as two separate sorted events.
# Use two pointers — one for arrivals, one for departures.
#
# At each step, take whichever event comes next:
#   - If next event is an arrival   → need one more platform (+1)
#   - If next event is a departure  → free up one platform  (-1)
#
# The maximum value of "platforms in use" at any point is the answer.
#
# Why this works: we only care about how many trains are simultaneously
# present, not which specific trains they are. Sorting both arrays and
# scanning them like a merge step gives us every overlap in O(n log n).

def min_platforms_optimal(arr, dep):
    arr.sort()
    dep.sort()

    n = len(arr)
    i = 0         # pointer into arrival times
    j = 0         # pointer into departure times

    platforms     = 0
    max_platforms = 0

    while i < n:
        if arr[i] <= dep[j]:   # next event is an arrival
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:                   # next event is a departure
            platforms -= 1
            j += 1

    return max_platforms


arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]
print(min_platforms_optimal(arr, dep))   # 3

arr2 = [1020, 1200]
dep2 = [1050, 1230]
print(min_platforms_optimal(arr2, dep2))  # 1


# ------------------------------------------------------------
# Trace for the first example:
#
# Sorted arr: [900, 945, 955, 1100, 1500, 1800]
# Sorted dep: [920, 1130, 1150, 1200, 1900, 2000]
#
# arr[0]=900  <= dep[0]=920  → platforms=1  (train 1 arrives)
# arr[1]=945  <= dep[0]=920? No → dep[0]=920 departs → platforms=0, j=1
# arr[1]=945  <= dep[1]=1130 → platforms=1  (train 2 arrives)
# arr[2]=955  <= dep[1]=1130 → platforms=2  (train 3 arrives)
# arr[3]=1100 <= dep[1]=1130 → platforms=3  (train 4 arrives)  ← MAX
# arr[4]=1500 <= dep[1]=1130? No → dep[1]=1130 departs → platforms=2, j=2
# arr[4]=1500 <= dep[2]=1150? No → dep[2]=1150 departs → platforms=1, j=3
# arr[4]=1500 <= dep[3]=1200? No → dep[3]=1200 departs → platforms=0, j=4
# arr[4]=1500 <= dep[4]=1900 → platforms=1  (train 5 arrives)
# arr[5]=1800 <= dep[4]=1900 → platforms=2  (train 6 arrives)
# i == n → stop
#
# Answer: 3
# ------------------------------------------------------------
