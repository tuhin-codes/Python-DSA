class Solution:
    def findPeakGrid(self, mat):

        rows = len(mat)
        cols = len(mat[0])

        low = 0
        high = cols - 1

        while low <= high:

            mid = (low + high) // 2

            # Find row having maximum element in middle column
            maxRow = 0
            for i in range(rows):
                if mat[i][mid] > mat[maxRow][mid]:
                    maxRow = i

            # Left neighbour
            if mid == 0:
                left = -1
            else:
                left = mat[maxRow][mid - 1]

            # Right neighbour
            if mid == cols - 1:
                right = -1
            else:
                right = mat[maxRow][mid + 1]

            # Peak found
            if mat[maxRow][mid] > left and mat[maxRow][mid] > right:
                return [maxRow, mid]

            # Move left
            elif left > mat[maxRow][mid]:
                high = mid - 1

            # Move right
            else:
                low = mid + 1