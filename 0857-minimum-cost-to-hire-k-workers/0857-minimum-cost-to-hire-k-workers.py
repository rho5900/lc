import heapq
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        ars = []
        for x,y in zip(quality,wage):
            ars.append([float(y)/x,x])
        ars.sort()
        maxheap = []
        mins = float('inf')
        wages = 0
        for x,y in ars:
            heapq.heappush(maxheap,-y)
            wages += y
            if len(maxheap) > k:
                y = heapq.heappop(maxheap)
                wages += y
            if len(maxheap) == k:
                cost = x * wages
                mins = min(cost, mins)
        return mins
