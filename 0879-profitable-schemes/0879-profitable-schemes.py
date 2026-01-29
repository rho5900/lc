class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        #at most n members in a crime
        #minprofit
        mods = 10**9 + 7
        x = n + 1
        y = minProfit + 1
        dp = [[0] * y for _ in range(x)]
        #0000
        #0000
        #0011
        #0000
        #0001
        #0000
        #100 * 100 * 100
        dp[0][0] = 1
        x = 0
        y = 0
        for x in range(len(group)):
            grouplen = group[x]
            p = profit[x]
            dpnew = [row[:] for row in dp]  
            for y in range(len(dp)):
                for z in range(len(dp[0])):
                    if dpnew[y][z] >= 1:
                        if grouplen + y <= len(dp)-1:
                            bucketx = grouplen + y
                            buckety = min(len(dp[0]) - 1,p + z)
                            dp[bucketx][buckety] = (dp[bucketx][buckety] + dpnew[y][z]) % mods      
        res = 0
        for x in dp:
            res += x[-1]%mods
        return res%mods

        """
        [0, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0]
        """




        