import collections
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans = []
        # hashMap = {}
        # for item in strs:
        #     sortItem = ''.join(sorted(item))
        #     if sortItem in hashMap:
        #         ans[hashMap[sortItem]].append(item)
        #     else:
        #         hashMap[sortItem] = len(ans)
        #         ans.append([item])
        # return ans
        mp = collections.defaultdict(list)
        for st in strs:
            key = ''.join(sorted(st))
            mp[key].append(st)
        return list(mp.values())

s = Solution()
print(s.groupAnagrams(strs = ["eat", "tea", "tan", "ate", "nat", "bat"]))