class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) + 1
        n = len(text2) + 1

        dp = [[0] * m for _ in range(n)]
        #a,b,c,d,e
        #a,c,e
        #0,0,0,0,0,0
        #0,1,0,0,0,0
        #0,1,1,0,0,0
        #0,0,0,0,0,0
        for x in range(1,len(dp)):
            for y in range(1,len(dp[0])):
                maxs = max(dp[x-1][y],dp[x][y-1])
                if text1[y-1] == text2[x-1]:
                    dp[x][y] = dp[x-1][y-1] + 1
                else:
                    dp[x][y] = maxs
        
        res = dp[-1][-1]
        return res
