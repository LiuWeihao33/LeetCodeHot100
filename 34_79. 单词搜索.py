from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backTrack(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            result = False
            visited.add((i, j))
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < row and 0 <= newj < col and (newi, newj) not in visited:
                    if backTrack(newi, newj, k + 1):
                        result = True
                        break
            visited.remove((i, j))
            return result


        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        row, col = len(board), len(board[0])

        for i in range(row):
            for j in range(col):
                if backTrack(i, j, 0):
                    return True
        return False

s = Solution()
print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))