class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        even_numbers = 0
        for i in range(1, len(nums)):
            if (sum(nums[:i]) - sum(nums[i:len(nums) + 1])) % 2 == 0:
                even_numbers += 1
        return even_numbers