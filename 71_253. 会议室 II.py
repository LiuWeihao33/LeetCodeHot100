import heapq
from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(rooms, intervals[0][1])
        for meet in intervals[1:]:
            if meet[0] >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, meet[1])
        return len(rooms)

s = Solution()
print(s.minMeetingRooms(intervals = [[0,30],[5,10],[15,20]]))