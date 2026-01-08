class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for x in range(len(digits)-1,-1,-1):
            if digits[x] != 9:
                digits[x] += 1
                return digits
            else:
                digits[x] = 0
                if x == 0:
                    digits.insert(0,1)
        return digits
        