class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        same = k        
        diff = k*(k-1)  
        
        for x in range(2, n):
            same, diff = diff, (same + diff) * (k-1)
        
        return same + diff