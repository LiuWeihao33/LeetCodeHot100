from typing import  List
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = 0
        indeg = [0] * numCourses
        edges = collections.defaultdict(list)
        for item in prerequisites:
            indeg[item[0]] += 1
            edges[item[1]].append(item[0])
        queue = collections.deque([i for i in range(numCourses) if indeg[i] == 0])

        while queue:
            visited += 1
            u = queue.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v)
        return True if visited == numCourses else False

s = Solution()
print(s.canFinish(numCourses = 2, prerequisites = [[1,0]]))