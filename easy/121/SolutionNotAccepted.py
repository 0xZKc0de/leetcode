class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        arr = []
        for i in range(1, len(prices)):
            for j in range(0, i):
                arr.append(prices[i] - prices[j])
        
        arr.sort()
        return arr[-1] if arr[-1] >= 0 else 0



# the complexity of this code is O(N*N), so he did not passed all the tests.