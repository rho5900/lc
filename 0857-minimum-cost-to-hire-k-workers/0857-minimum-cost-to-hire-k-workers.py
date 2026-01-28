import heapq
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        ars = []
        for x,y in zip(quality,wage):
            ars.append([float(y)/x,x])
        ars.sort()
        maxheap = []
        mins = float('inf')
        for x,y in ars:
            heapq.heappush(maxheap,-y)
            if len(maxheap) > k:
                heapq.heappop(maxheap)
            if len(maxheap) == k:
                sums = -sum(maxheap)
                cost = x * sums
                mins = min(cost, mins)
        return mins
