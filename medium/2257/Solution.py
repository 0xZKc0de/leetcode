class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2
            
        for r, c in guards:
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 1 or grid[nr][nc] == 2:
                        break
                    grid[nr][nc] = 3
                    nr += dr
                    nc += dc
                    
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    count += 1
        
        return count