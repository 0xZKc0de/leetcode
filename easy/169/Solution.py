from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = Counter(nums)
        result = 0
        count = 0
        for key, value in dict.items():
            if value > count:
                count = value
                result = key
        return result
    

    