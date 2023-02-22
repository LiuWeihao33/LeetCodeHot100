class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        def backTrack(index):
            if index == len(digits):
                combines.append(''.join(combine))
            else:
                num = digits[index]
                for s in phoneMap[num]:
                    combine.append(s)
                    backTrack(index + 1)
                    combine.pop()


        if not digits:
            return []
        phoneMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        combine = []
        combines = []
        backTrack(0)
        return combines

s = Solution()
print(s.letterCombinations(digits = "2"))

