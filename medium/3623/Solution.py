from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        y_groups = defaultdict(int)
        for x, y in points:
            y_groups[y] += 1

        counts = [c for c in y_groups.values() if c >= 2]
        
        n = len(counts)
        if n < 2:
            return 0

        ways = []
        for c in counts:
            ways.append((c * (c - 1)) // 2)
            
        total_trapezoids = 0
    
        
        sum_ways = 0
        sum_sq_ways = 0
        
        for w in ways:
            sum_ways = (sum_ways + w) % MOD
            sum_sq_ways = (sum_sq_ways + (w * w)) % MOD
            
        
        sum_ways_sq = (sum_ways * sum_ways) % MOD
  
        diff = (sum_ways_sq - sum_sq_ways + MOD) % MOD

        total_trapezoids = (diff * pow(2, -1, MOD)) % MOD
        
        return total_trapezoids