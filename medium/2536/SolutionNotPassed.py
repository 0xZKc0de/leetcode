class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        arr = [[0 for _ in range(n)] for _ in range(n)]
        for element in queries:
            for i in range(element[0], (element[2]) + 1):
                for j in range(element[1], (element[3]) + 1):
                    arr[i][j] +=1
        
        return arr


# this solution did not pass all the tests

