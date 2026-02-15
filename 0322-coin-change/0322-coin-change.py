class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        #amt / coin[i]
        #1,2
        #3
        @lru_cache(maxsize = None)
        def dfs(i,amt):
            if i >= len(coins):
                return float('inf')
            if amt > amount:
                return float('inf')
            if amt == amount:
                return 0
            noskip = 1 + dfs(i,amt + coins[i])
            skip = dfs(1+i,amt)
            return min(noskip,skip)
        return dfs(0,0) if dfs(0,0) != float('inf') else -1