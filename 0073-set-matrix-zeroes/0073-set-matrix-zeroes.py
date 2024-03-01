class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        pos = []
        for i in range(m): # 1. 0의 위치 검사 O(m*n)
            for j in range(n):
                if matrix[i][j] == 0: pos.append([i, j])

        for (x, y) in pos: # 2. 상하좌우 0으로 만들기 O(0의개수*(m+n))
            for i in range(m): matrix[i][y] = 0
            for i in range(n): matrix[x][i] = 0


        