from collections import defaultdict
from typing import List


class Solution:

  def largestInteger(self, nums: List[int], k: int) -> int:
    subarray_counts = defaultdict(int)
    n = len(nums)
    for i in range(n - k + 1):
      unique_in_subarray = set(nums[i : i + k])
      for num in unique_in_subarray:
        subarray_counts[num] += 1

    ans = -1
    for num, count in subarray_counts.items():
      if count == 1:
        ans = max(ans, num)

    return ans
