from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        ld = Counter(nums)
        for key, value in ld.items():
            if value != 1:
                return key