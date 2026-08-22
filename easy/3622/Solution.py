class Solution:
    def checkDivisibility(self, n: int) -> bool:
        string = str(n)
        s , p = 0, 1
        for element in string:
            s += int(element)
            p *= int(element)
        return True if n % (s + p) == 0 else False
        
