import math
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        """
        if n == 1:
            return k
        if n == 2:
            return k * k
        #n length
        # k colors
        #n = 3
        #k = 2

        res = 0
        p = 0
        
        for x in range(0,(n//3)):
            #x is how many clumps of 3 we have
            # k choose x to find how the combo of colors
            #(n-k)*3 + x and then factorial that
            combos = math.factorial(k) / ((math.factorial(x+1) * math.factorial(k-(x+1))))
            di = (n-(x+1)*3) + x+1
            #print(di)
            combos = combos * math.factorial(di)
            # n - (3 * clumps)
            if p % 2 == 0:
                res += combos
            else:
                res -= combos
            print(res)
            p += 1
        total = k**n
        return total - res
        """
        if n == 1:
            return k
        if n == 2:
            return k*k
        dp = [k,k*k]
        dp = [0]*n
        dp[0] = k
        dp[1] = k * k
        same = k
        dif = k * (k-1)
        for x in range(2,n):
            new_same = dif
            new_dif = (same + dif) * (k-1)

            same = new_same
            dif = new_dif
            dp[x] = same + dif
        return dp[-1]

        #b,b,b,r,r,r,r


