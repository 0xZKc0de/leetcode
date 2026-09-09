class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        if n <= 999 :
            return res

        elif n > 999 and n <= 1000000:
            res = n - 999
            return res if n != 1000000 else res +  1

        elif n > 1000000 and n <= 1000000000 :
            res =  999999 - 999 + ( n - 999999 ) * 2
            return res if n != 1000000000 else res + 1
            
        elif n > 1000000000 and n <= 1000000000000 :
            res = 999999 - 999 + ( 999999999 - 999999 ) * 2 + (n - 999999999) * 3
            return res if n != 1000000000000 else res + 1

        else :
            res = 999999 - 999 + ( 999999999 - 999999 ) * 2 + (999999999999 - 999999999) * 3 + (n - 999999999999) * 4
            return res if n != 1000000000000000 else res + 1
        
        
