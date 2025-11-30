from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target = total_sum % p
        
        if target == 0:
            return 0
        
        mod_map = {0: -1}
        current_sum = 0
        min_len = len(nums)
        for i, num in enumerate(nums):
            current_sum = (current_sum + num) % p
            
            needed = (current_sum - target + p) % p
        
            if needed in mod_map:
                length = i - mod_map[needed]
                min_len = min(min_len, length)
            

            mod_map[current_sum] = i
            
        return min_len if min_len < len(nums) else -1