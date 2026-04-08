# Job Sequencing Problem
#
# Given N jobs, each with a deadline and profit, find the maximum number
# of jobs that can be completed and the maximum profit.
# Rules:
#   - Each job takes exactly 1 unit of time
#   - Only one job can run at a time
#   - A job must finish by its deadline (time slots are 1-indexed)
#   - Profit is earned only if the job is completed within its deadline
#
# Examples:
#   jobs = [(1,4,20), (2,1,10), (3,1,40), (4,1,30)]   format: (id, deadline, profit)
#   Output: (2, 60)   → job 3 (slot 1) + job 1 (slot 2..4), profit = 40+20
#
#   jobs = [(1,2,100), (2,1,19), (3,2,27), (4,1,25), (5,1,15)]
#   Output: (2, 127)  → job 1 (slot 2) + job 3 (slot 1), profit = 100+27

# ------------------------------------------------------------
# GREEDY  —  O(n^2) time | O(n) space
# ------------------------------------------------------------
# Strategy:
#   1. Sort jobs by profit descending (take the most valuable job first)
#   2. For each job, try to assign it to the LATEST available slot
#      that is still <= its deadline
#      (latest slot = keeps earlier slots free for jobs with tighter deadlines)
#   3. If no slot is available → skip the job
#
# Why greedy works: taking higher-profit jobs first and placing them as
# late as possible maximises profit while leaving room for jobs with
# earlier deadlines.

class Solution(object):
    def jobScheduling(self, jobs, n):
        # Sort jobs by profit (descending)
        jobs.sort(key=lambda x: x[2], reverse=True)

        # Find maximum deadline
        max_deadline = max(job[1] for job in jobs)

        # slots[t] = job_id scheduled at time slot t  (-1 = free)
        slots = [-1] * (max_deadline + 1)

        job_count  = 0
        max_profit = 0

        for job_id, deadline, profit in jobs:
            # Try to place in the latest free slot <= deadline
            for t in range(deadline, 0, -1):
                if slots[t] == -1:
                    slots[t] = job_id
                    job_count  += 1
                    max_profit += profit
                    break

        return (job_count, max_profit)


# Tests
sol = Solution()

n1   = 4
jobs1 = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
print(sol.jobScheduling(jobs1, n1))   # (2, 60)

n2   = 5
jobs2 = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 1, 15)]
print(sol.jobScheduling(jobs2, n2))   # (2, 127)


# ------------------------------------------------------------
# Trace for Example 1:
#
# Sorted by profit: [(3,1,40), (4,1,30), (1,4,20), (2,1,10)]
# max_deadline = 4,  slots = [-1, -1, -1, -1, -1]  (indices 0..4)
#
# Job 3 (deadline=1, profit=40):
#   t=1 → free → slots[1]=3, count=1, profit=40
#
# Job 4 (deadline=1, profit=30):
#   t=1 → taken → no free slot → skip
#
# Job 1 (deadline=4, profit=20):
#   t=4 → free → slots[4]=1, count=2, profit=60
#
# Job 2 (deadline=1, profit=10):
#   t=1 → taken → skip
#
# Result: (2, 60) ✓
# ------------------------------------------------------------
