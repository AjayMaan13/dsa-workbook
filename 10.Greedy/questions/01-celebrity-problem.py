# Celebrity Problem (Hard)
# (Elimination / candidate reduction problem)
#
# Problem Statement:
# A celebrity is a person who is known by everyone else at the party
# but does not know anyone in return.
# Given a square matrix M of size N x N where M[i][j] is 1 if person i
# knows person j, and 0 otherwise, determine if there is a celebrity.
# Return the index of the celebrity or -1 if no such person exists.
# Note: M[i][i] is always 0.
#
# Example 1:
#   Input:  M = [[0,1,1,0],[0,0,0,0],[1,1,0,0],[0,1,1,0]]
#   Output: 1
#   Explanation: Person 1 knows no one and is known by 0, 2, 3.
#
# Example 2:
#   Input:  M = [[0,1],[1,0]]
#   Output: -1
#   Explanation: Both persons know each other → no celebrity.


# ─────────────────────────────────────────────
# Brute Force  ·  O(n²) time  ·  O(n) space
# ─────────────────────────────────────────────
# Algorithm:
# 1. Build two arrays: knowMe[i] = how many people know i
#                      Iknow[i]  = how many people i knows
# 2. Scan the full matrix once to fill both arrays.
# 3. Any person where knowMe[i] == n-1 and Iknow[i] == 0 is the celebrity.

class BruteForceSolution:
    def celebrity(self, M):
        n = len(M)
        knowMe = [0] * n   # count of people who know person i
        Iknow  = [0] * n   # count of people person i knows

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    knowMe[j] += 1
                    Iknow[i]  += 1

        for i in range(n):
            if knowMe[i] == n - 1 and Iknow[i] == 0:
                return i

        return -1


# ─────────────────────────────────────────────
# Optimal  ·  O(n) time  ·  O(1) space
# ─────────────────────────────────────────────
# Algorithm (two-pointer elimination):
# 1. Start with top = 0, down = n-1.
# 2. While top < down:
#      - If top knows down  → top cannot be celebrity → top += 1
#      - Elif down knows top → down cannot be celebrity → down -= 1
#      - Else neither knows each other → both eliminated → top += 1, down -= 1
# 3. After the loop, `top` is the sole candidate.
#    Verify: everyone knows top AND top knows no one.
# 4. Return top if valid, else -1.

class OptimalSolution:
    def celebrity(self, M):
        n = len(M)
        top, down = 0, n - 1

        while top < down:
            if M[top][down] == 1:       # top knows down → top is not celebrity
                top += 1
            elif M[down][top] == 1:     # down knows top → down is not celebrity
                down -= 1
            else:                       # neither knows the other → both out
                top += 1
                down -= 1

        if top > down:
            return -1

        # Validate candidate
        for i in range(n):
            if i == top:
                continue
            if M[top][i] == 1 or M[i][top] == 0:   # top knows someone OR someone doesn't know top
                return -1

        return top


# ─────────────────────────────────────────────
# Driver
# ─────────────────────────────────────────────
if __name__ == "__main__":
    M = [
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
    ]

    print("Brute Force →", BruteForceSolution().celebrity(M))   # 1
    print("Optimal     →", OptimalSolution().celebrity(M))      # 1
