# 455. Assign Cookies
# https://leetcode.com/problems/assign-cookies/
#
# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
#
# Each child i has a greed factor g[i], which is the minimum size of a cookie
# that the child will be content with; and each cookie j has a size s[j].
# If s[j] >= g[i], we can assign the cookie j to the child i, and the child i
# will be content. Your goal is to maximize the number of your content children
# and output the maximum number.
#
# Example 1:
#   Input: g = [1,2,3], s = [1,1]
#   Output: 1
#   Explanation: You have 3 children and 2 cookies. The greed factors are 1,2,3.
#   Both cookies have size 1, so only the child with greed factor 1 is satisfied.
#
# Example 2:
#   Input: g = [1,2], s = [1,2,3]
#   Output: 2
#   Explanation: Both children can be satisfied.
#
# Constraints:
#   1 <= g.length <= 3 * 10^4
#   0 <= s.length <= 3 * 10^4
#   1 <= g[i], s[j] <= 2^31 - 1


# Brute Force - O(n^2) time, O(n) space
# Sort both arrays, then for each child try every cookie until we find one that satisfies them.
# A used[] flag prevents assigning the same cookie twice.
class Solution:
    def findContentChildren(self, g, s):
        if not g or not s:
            return 0

        g.sort()
        s.sort()
        used = [False] * len(s)

        count = 0

        for i in range(len(g)):
            cur = g[i]

            for j in range(len(s)):
                if not used[j] and s[j] >= cur:  # smallest unused cookie that satisfies child i
                    used[j] = True
                    count += 1
                    break

        return count


# Optimal Greedy - O(n log n) time, O(1) space
# Sort both arrays. Use two pointers: try to satisfy the least greedy child with the smallest cookie.
# If the cookie is big enough, move both pointers (child is satisfied).
# If not, move only the cookie pointer (try a bigger cookie for the same child).
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        i = j = 0
        count = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:   # cookie j satisfies child i
                count += 1
                i += 1         # move to next child
            j += 1             # always move to next cookie

        return count


g = [1, 2, 3]
s = [1, 1]
sol = Solution()
print(sol.findContentChildren(g, s))  # 1
