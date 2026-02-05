class Solution:
    def countMonobit(self, n: int) -> int:
        #1,2,4,8,16
        #1,3,7,15,31
        #2,3,4,5,6,7,8,9,10
        #2^x -1

        sqr = 0
        cnts = 0
        for x in range(0,n+1):
            p = 2**sqr
            if x + 1 == p:
                cnts += 1
                sqr += 1
        return cnts