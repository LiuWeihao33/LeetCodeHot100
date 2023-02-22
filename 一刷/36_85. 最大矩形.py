from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 先计算前缀和
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        pre = [0] * col
        result = 0
        for i in range(row):
            for j in range(col):
                if i == 0:
                    pre[j] = int(matrix[i][j])
                else:
                    pre[j] = pre[j] + 1 if matrix[i][j] == '1' else 0

            # 再单调栈
            left, right = [0] * col, [0] * col
            mono_stack = list()
            for k in range(col):
                while mono_stack and pre[mono_stack[-1]] >= pre[k]:
                    mono_stack.pop()
                left[k] = mono_stack[-1] if mono_stack else -1
                mono_stack.append(k)

            mono_stack = list()
            for k in range(col-1, -1, -1):
                while mono_stack and pre[mono_stack[-1]] >= pre[k]:
                    mono_stack.pop()
                right[k] = mono_stack[-1] if mono_stack else col
                mono_stack.append(k)

            ans = max((right[k] - left[k] - 1) * pre[k] for k in range(col)) if col > 0 else 0
            result = max(result, ans)
        return result

s = Solution()
print(s.maximalRectangle(matrix = [["0","0"]]))