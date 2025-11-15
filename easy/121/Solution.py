class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        sell, buy, result = prices[0], 0, 0
        for i in range(1, len(prices)):
            if sell > prices[i]:
                sell = prices[i] 
            else:
                buy = prices[i]
                result = max(result, buy - sell)
        return result


# Now this solution with O(N) Complexity.