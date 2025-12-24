from bisect import bisect_right
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        
        suffix_max = [0] * n
        suffix_max[-1] = events[-1][2]
        
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(events[i][2], suffix_max[i+1])
            
        starts = [e[0] for e in events]
        max_sum = 0
        
        for i in range(n):
            current_val = events[i][2]
            idx = bisect_right(starts, events[i][1])
            
            if idx < n:
                max_sum = max(max_sum, current_val + suffix_max[idx])
            else:
                max_sum = max(max_sum, current_val)
                
        return max_sum