class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]
        dp[d][n] = 0

        for day in range(d - 1, -1, -1):
            for left in range(day, n - (d - day - 1)):
                maxs = float('-inf')
                for x in range(left, n - (d - day - 1)):
                    maxs = max(maxs, jobDifficulty[x])
                    dp[day][left] = min(dp[day][left], maxs + dp[day + 1][x + 1])

        return dp[0][0] if dp[0][0] != float('inf') else -1