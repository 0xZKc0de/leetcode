import collections
import heapq
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        n = len(nums)
        answer = []
        
        def get_x_sum(sub: List[int]) -> int:
            counts = collections.Counter(sub)
            
            if len(counts) < x:
                return sum(sub)
            
            items = counts.items()
            
            top_x_items = heapq.nlargest(x, items, key=lambda item: (item[1], item[0]))
            
            total_sum = 0
            for val, freq in top_x_items:
                total_sum += val * freq
                
            return total_sum
        
        for i in range(n - k + 1):
            subarray = nums[i : i + k]
            current_x_sum = get_x_sum(subarray)
            answer.append(current_x_sum)
            
        return answer