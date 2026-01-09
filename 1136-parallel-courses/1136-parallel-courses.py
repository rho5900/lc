from collections import deque
class Solution(object):
    def minimumSemesters(self, n, relations):
        """
        :type n: int
        :type relations: List[List[int]]
        :rtype: int
        """
        myset = set()
        maps = defaultdict(list)
        for x,y in relations:
            maps[x].append(y)
        
        mymap = {}
        for x,y in relations:
            if x not in mymap:
                mymap[x] = 0
            if y not in mymap:
                mymap[y] = 1
            else:
                mymap[y] += 1
        for y in range(1,n+1):
            if y not in mymap:
                mymap[y] = 0
        queue = deque()
        for x in mymap:
            if mymap[x] == 0:
                queue.append(x)
                myset.add(x)
        if len(queue) == 0:
            return -1
        cts = 0
        visited = 0
        while queue:
            cts += 1
            lens = len(queue)
            for _ in range(lens):
                node = queue.popleft()
                visited += 1
                for p in maps[node]:
                    neighbor = p
                    mymap[p] -= 1
                    if mymap[p] == 0:
                        queue.append(neighbor)

        if visited < n:
            return -1
        return cts