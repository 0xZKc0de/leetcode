class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(0, max([sum(gain[:i]) for i in range(1, len(gain) +1)]))

