# Shortest Job First (SJF) CPU Scheduling
# (Classic Greedy)
#
# Problem Statement:
# Given a list of job durations, implement the Shortest Job First scheduling
# algorithm and return the average waiting time across all jobs.
#
# The waiting time for a job = total duration of all jobs that ran before it.
# Average waiting time = sum of all waiting times / number of jobs.
#
# Example 1:
#   Input:  jobs = [3, 1, 4, 2, 5]
#   Sorted: [1, 2, 3, 4, 5]
#   Waits:  [0, 1, 3, 6, 10]  → sum = 20  → avg = 20 // 5 = 4
#
# Example 2:
#   Input:  jobs = [4, 3, 7, 1, 2]
#   Sorted: [1, 2, 3, 4, 7]
#   Waits:  [0, 1, 3, 6, 10] → sum = 20  → avg = 20 // 5 = 4


# Greedy - O(n log n) time, O(1) extra space
#
# Key insight: always run the shortest remaining job next.
# Any swap of two adjacent jobs where the longer one runs first increases the
# waiting time of the shorter one without reducing anyone else's — so sorting
# ascending is the provably optimal order to minimise total waiting time.

class Solution:
    def sjf(self, jobs):
        # sort ascending so the shortest job executes first
        jobs.sort()

        total_wait = 0    # sum of waiting times across all jobs
        current_time = 0  # tracks when the CPU becomes free (= elapsed duration so far)

        for job in jobs:
            # this job waits for everything that ran before it
            total_wait += current_time

            # after this job finishes, the clock advances by its duration
            current_time += job

        # integer average (floor division as expected by the problem)
        return total_wait // len(jobs)


# Driver
if __name__ == "__main__":
    sol = Solution()
    print(sol.sjf([3, 1, 4, 2, 5]))   # 4
    print(sol.sjf([4, 3, 7, 1, 2]))   # 4
