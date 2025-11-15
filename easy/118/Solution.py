class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        arr = [[1]]
        
        for i in range(1, numRows):
            prev_row = arr[i-1]
            
            new_row_half = [1]
            row_len = i + 1
            half_len = (row_len + 1) // 2
            
            for j in range(1, half_len):
                val = prev_row[j-1] + prev_row[j]
                new_row_half.append(val)

            if row_len % 2 == 0:
                reversed_part = new_row_half[::-1]
            else:
                reversed_part = new_row_half[:-1][::-1]
            
            full_new_row = new_row_half + reversed_part
            arr.append(full_new_row)

        return arr