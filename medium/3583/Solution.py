from collections import Counter
from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        ans = 0
        right = Counter(nums)
        left = Counter()
        
        for x in nums:
            right[x] -= 1
            
            target = x * 2
  
            l_cnt = left[target]
            r_cnt = right[target]
            
            if l_cnt > 0 and r_cnt > 0:
                ans = (ans + l_cnt * r_cnt) % MOD
            left[x] += 1
            
        return ans