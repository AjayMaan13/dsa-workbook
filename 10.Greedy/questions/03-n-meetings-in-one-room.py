# N Meetings in One Room
# (Classic Greedy - Activity Selection)
#
# Problem Statement:
# There is one meeting room. Given two arrays start[] and end[] of size N,
# where start[i] and end[i] are the start and end times of the i-th meeting,
# find the maximum number of meetings that can be held. Only one meeting can
# occupy the room at a time. Print the 1-indexed order of selected meetings.
#
# Example 1:
#   Input: start = [1,3,0,5,8,5], end = [2,4,5,7,9,9]
#   Output: [1, 2, 4, 5]
#
# Example 2:
#   Input: start = [1,5], end = [7,8]
#   Output: [1]


# Greedy - O(n log n) time, O(n) space
#
# Key insight: always pick the meeting that ends earliest among the remaining
# valid ones. An early finish leaves the room free for as many future meetings
# as possible — this greedy choice is provably optimal (activity selection).
#
# Steps:
#   1. Pair each meeting with its end time and original 1-based index.
#   2. Sort by end time (stable sort handles ties consistently).
#   3. Greedily select a meeting if its start time is strictly after the
#      last selected meeting's end time.

class Solution:
    def maxMeetings(self, start, end):
        # build (end_time, start_time, 1-based index) for each meeting
        meetings = [(end[i], start[i], i + 1) for i in range(len(start))]

        # sort by end time so earliest-finishing meetings come first
        meetings.sort()

        result = []
        last_end = -1          # end time of the most recently selected meeting

        for e, s, idx in meetings:
            # meeting is compatible only if it starts after the last one ends
            if s > last_end:
                result.append(idx)
                last_end = e   # room is now occupied until time e

        return result


# Driver
if __name__ == "__main__":
    sol = Solution()

    start1, end1 = [1, 3, 0, 5, 8, 5], [2, 4, 5, 7, 9, 9]
    print(sol.maxMeetings(start1, end1))   # [1, 2, 4, 5]

    start2, end2 = [1, 5], [7, 8]
    print(sol.maxMeetings(start2, end2))   # [1]
