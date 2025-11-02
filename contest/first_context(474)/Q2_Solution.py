class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = []
        for element in nums:
            result.append(abs(element))
        result.sort()
        return pow(10, 5)*result[-1]*result[-2]
            ©leetcode
