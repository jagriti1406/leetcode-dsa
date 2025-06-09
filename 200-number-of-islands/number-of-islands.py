class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visit = set()
        directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]

        def dfs(r, c):
            q = deque()

            q.append((r, c))
            grid[r][c] = "0"
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                        continue
                    q.append((r, c))
                    grid[r][c] = "0"

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visit:
                    dfs(i, j)
                    count += 1
        return count
