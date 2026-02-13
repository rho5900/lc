class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        day = 0
        #len(jobDifficulty) - d-1
        #left 
        #day were on
        if len(jobDifficulty) < d:
            return -1
        @lru_cache(2000)
        
        def dfs(left,days):
            
            if days == d:
                return 0 if left == len(jobDifficulty) else float('inf')
            if left >= len(jobDifficulty):
                return float('inf')
            #len(jobDifficulty) - d - days - 1
            maxs = float('-inf')
            ars = []
            for x in range(left,len(jobDifficulty)):
                if jobDifficulty[x] > maxs:
                    maxs = jobDifficulty[x]
                ars.append(maxs+dfs(x+1,days + 1))

            return min(ars)
        
        return dfs(0,0)
                