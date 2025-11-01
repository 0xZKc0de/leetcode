class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefixSum = []
        sum = 0
        for element in nums:
            sum += element
            prefixSum.append(sum)
        prefixSum.sort()
        if(prefixSum[0] < 0):
            return abs(prefixSum[0] -1)
        else:
            return 1


# Time Complexity : O(NlogN).
# using prefix sum to solve this problem.
