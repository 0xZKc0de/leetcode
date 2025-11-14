class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        

        for r1, c1, r2, c2 in queries:
            mat[r1][c1] += 1
            mat[r1][c2 + 1] -= 1
            mat[r2 + 1][c1] -= 1
            mat[r2 + 1][c2 + 1] += 1
            
        for i in range(n):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]

        for j in range(n):
            for i in range(1, n): 
                mat[i][j] += mat[i - 1][j]

        arr = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                arr[i][j] = mat[i][j]
                
        return arr