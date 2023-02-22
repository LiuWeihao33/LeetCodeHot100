from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key=lambda x:x[0], reverse=False)
        a = sorted(intervals, key=lambda x:x[0], reverse=False)
        ans = []
        for item in a:
            if not ans or ans[-1][1] < item[0]:
                ans.append(item)
            else:
                ans[-1][1] = max(ans[-1][1], item[1])
        return ans

s = Solution()
print(s.merge(intervals = [[1,3],[8,10], [2,6],[15,18]]))