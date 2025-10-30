class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles == 0 or numBottles < numExchange:
            return numBottles
        result, numEmpty = numBottles, numBottles
        while numExchange <= numEmpty:
            numBottles = int(numEmpty / numExchange)
            numEmpty = numEmpty - numBottles*numExchange
            result +=numBottles
            numEmpty +=numBottles
        
        return result


# There is no specific algorithm or pattern in this problem, just a simple maths.
