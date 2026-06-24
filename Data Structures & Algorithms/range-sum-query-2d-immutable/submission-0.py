class NumMatrix:

    def __init__(self, matrix):

        ROWS = len(matrix)
        COLS = len(matrix[0])

        self.prefix = [[0]*(COLS+1)
                        for _ in range(ROWS+1)]

        for r in range(ROWS):
            for c in range(COLS):

                self.prefix[r+1][c+1] = (
                    matrix[r][c]
                    + self.prefix[r][c+1]
                    + self.prefix[r+1][c]
                    - self.prefix[r][c]
                )

    def sumRegion(self, row1, col1, row2, col2):

        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        bottomRight = self.prefix[row2][col2]

        above = self.prefix[row1-1][col2]

        left = self.prefix[row2][col1-1]

        overlap = self.prefix[row1-1][col1-1]

        return bottomRight - above - left + overlap