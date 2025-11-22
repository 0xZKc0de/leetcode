class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for element in nums:
            if element % 3 == 1:
                element  -= 1
                count += 1
            if element % 3 == 2:
                element += 1
                count += 1
        return count
        
        