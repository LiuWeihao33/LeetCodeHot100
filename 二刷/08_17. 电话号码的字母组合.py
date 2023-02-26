from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        def backTrack(digit, tmp):
            if len(tmp) == len(digits):
                ans.append(''.join(tmp))
                return
            for i in range(len(digit)):
                letters = numMap[digit[i]]
                for c in letters:
                    backTrack(digit[i+1:], tmp + [c])

        if not digits:
            return []
        ans = []
        backTrack(digits, [])
        return ans

s = Solution()
print(s.letterCombinations(digits = "23"))