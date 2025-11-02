class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()
        set_nums = set(nums)
        for i in range(nums[0], nums[-1]):
            if i not in set_nums:
                result.append(i)
        return result©leetcode
