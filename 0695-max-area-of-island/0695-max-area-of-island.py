class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        def f(i,j):
            if i < 0 or i>=R or j < 0 or j>=C or grid[i][j] ==0:
                return 0

            grid[i][j] = 0
            return 1+ f(i+1,j)+ f(i-1,j)+f(i, j+1)+f(i, j-1)
        ans = 0
        for i in range(R):
            for j in range(C):
                ans = max(ans, f(i,j))
        return ans