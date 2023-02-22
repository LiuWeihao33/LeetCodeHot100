class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque
        if n == 0:
            return 0
        queue = deque([n])
        step = 0
        visited = set()
        while(queue):
            step += 1
            l = len(queue)
            for _ in range(l):
                tmp = queue.pop()
                for i in range(1, int(tmp**0.5)+1):
                    x = tmp - i ** 2
                    if x == 0:
                        return step
                    if x not in visited:
                        queue.appendleft(x)
                        visited.add(x)
        return step