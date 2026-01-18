class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        a = 6 
        b = 6 
        
        for i in range(2, n + 1):
            
            new_a = (3 * a + 2 * b) % MOD
            new_b = (2 * a + 2 * b) % MOD
            
            a, b = new_a, new_b
        
        return (a + b) % MOD
        