class Solution(object):
    def paintWalls(self, cost, time):
        """
        :type cost: List[int]
        :type time: List[int]
        :rtype: int
        """
        """
        if len(cost) == 1:
            return cost[0]
        dc = []
        for x in range(len(cost)):
            dc.append([cost[x],time[x]])
        dc.sort(key = lambda i:i[0])
        ptr = len(cost)//2
        res = 0
        lefttime = 0
        righttime = 0
        for x in range(ptr):
            right = len(dc)-1 - x
            lefttime += dc[x][1]
            righttime += 1
            res += dc[x][0]
        if len(cost) % 2 != 0:
            if lefttime < righttime:
                res += dc[len(dc)//2 + 1][0]
        return res
        """
    


        #[10, 20, 24, 25, 26, 51, 53, 63]
        #[1,   2,  1,  2,  1,  1 ,1,   2]
        #0,0,0,0,0 case
        #0,0,0,0,0
        #0,0,0,0,0
        #0,0,0,0,0
        #0,0,0,0,0
        dp = [[2**31] * (len(cost) + 1) for _ in range(len(cost) +1)]
        dp[0][0] = 0
        #i,j i element j complete
        for x in range(1,len(dp)):
            for y in range(len(dp[0])):
                dp[x][y] = min(dp[x][y], dp[x-1][y])
                bucket = min(len(dp[0])-1,1 + time[x-1] + y)
                dp[x][bucket] = min(dp[x][bucket],cost[x-1] + dp[x-1][y])
        mins = 2**31
        for x in range(len(dp)):
            mins = min(mins,dp[x][len(dp[0]) - 1])
        return mins
