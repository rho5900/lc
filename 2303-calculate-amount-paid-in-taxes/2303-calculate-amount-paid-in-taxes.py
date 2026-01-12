class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        prev = -1
        res = 0
        for x in range(len(brackets)):
            p,q = brackets[x][0],brackets[x][1]
            q = float(q)/100
            print(q)
            if income == 0:
                return res
            if x == 0:
                prev = p
                if p == income:
                    res += p * q
                    return res
                elif p < income:
                    income -= p
                    res += p * q
                else:
                    res += income * q
                    return res
            else:
                p = brackets[x][0]-brackets[x-1][0]
                if p == income:
                    res += p * q
                    return res
                elif p < income:
                    income -= p
                    res += p * q
                else:
                    res += income * q
                    return res
        return res

