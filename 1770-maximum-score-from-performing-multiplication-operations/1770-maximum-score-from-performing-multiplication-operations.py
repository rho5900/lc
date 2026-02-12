class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        memo = [[float('inf')] * m for _ in range(m) ]
        

        #0,0,0
        #0,0,0
        #0,0,0
        #index left
        #how many weve taken from m
        m = len(multipliers)
        @lru_cache(2000)
        def dfs(left,cnt):
            if cnt == m:
                return 0
            mult = multipliers[cnt]
            r = len(nums) - 1 - (cnt - left)
            return max(mult * nums[left] + dfs(left + 1,cnt +1),mult * nums[r] + dfs(left,cnt+1))


        
        return dfs(0,0)



